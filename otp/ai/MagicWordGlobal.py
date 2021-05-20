MINIMUM_MAGICWORD_ACCESS = 300

class MagicError(Exception): pass

def ensureAccess(access, msg='Sorry! Insufficient access'):
    if spellbook.getInvokerAccess() < access:
        raise MagicError(msg)

class Spellbook:
    """
    The Spellbook manages the list of all Magic Words that have been registered
    anywhere in the system. When the MagicWordManager(AI) wants to process a
    Magic Word, it is passed off to the Spellbook, which performs the operation.

    To add Magic Words to the Spellbook, use the @magicWord() decorator.
    """

    def __init__(self):
        self.words = {}

        self.currentInvoker = None
        self.currentTarget = None

    def addWord(self, word):
        self.words[word.name.lower()] = word

    def process(self, invoker, target, incantation):
        self.currentInvoker = invoker
        self.currentTarget = target
        word, args = (incantation.split(' ', 1) + [''])[:2]

        try:
            return self.doWord(word, args)
        except MagicError as e:
            return e.message
        except Exception:
            return describeException(backTrace=1)
        finally:
            self.currentInvoker = None
            self.currentTarget = None

    def doWord(self, wordName, args):
        wordName = wordName.lower()
        word = self.words.get(wordName)
        if not word:
            return

        ensureAccess(word.access)
        if self.getTarget() and self.getTarget() != self.getInvoker():
            if self.getInvokerAccess() < self.getTarget().getAdminAccess():
                raise MagicError('Target must have lower or equal access')

        result = word.run(args)
        if result is not None:
            return str(result)

    def getInvoker(self):
        return self.currentInvoker

    def getTarget(self, required=0):
        if self.getInvokerAccess < required:
            return self.getInvoker()
        return self.currentTarget

    def getInvokerAccess(self):
        if not self.currentInvoker:
            return 0
        return self.currentInvoker.getAdminAccess()

    def __repr__(self):
        r = ''

        for name, word in self.words.items():
            r += '%s (%d)\n' % (name, word.access)

        return r

spellbook = Spellbook()

# CATEGORIES
class MagicWordCategory:
    def __init__(self, name, access):
        self.name = name
        self.access = access

CATEGORY_ANY = MagicWordCategory('Unrestricted commands', 0)
CATEGORY_BASIC = MagicWordCategory('Basic commands', 100)
CATEGORY_SUPPORTER = MagicWordCategory('Supporter', 110)
CATEGORY_CAPTAIN = MagicWordCategory('Captain', 120)
CATEGORY_PIRATE_LORD = MagicWordCategory('Pirate Lord', 130)
CATEGORY_PIRATE_KING = MagicWordCategory('Pirate King', 140)
CATEGORY_PIRATE_GOD = MagicWordCategory('Pirate God', 150)
CATEGORY_SPONSOR = MagicWordCategory('Game sponsor commands', 200)
CATEGORY_MEDIA_TEAM = MagicWordCategory('Media team commands', 300)
CATEGORY_STREAMER = MagicWordCategory('Streamer commands', 400)
CATEGORY_STAFF = MagicWordCategory('Basic staff commands', 500)
CATEGORY_MODERATION = MagicWordCategory('Moderation commands', 600)
CATEGORY_GAME_MASTER = MagicWordCategory('Game master commands', 700)
CATEGORY_GAME_DESIGNER = MagicWordCategory("Game designer commands", 800)
CATEGORY_GAME_DEVELOPER = MagicWordCategory('Game developer commands', 900)
CATEGORY_SYSTEM_ADMINISTRATOR = MagicWordCategory('System administrator commands', 1000)

class MagicWord:
    def __init__(self, name, func, types, access, doc):
        self.name = name
        self.func = func
        self.types = types
        self.access = access
        self.doc = doc

    def parseArgs(self, string):
        maxArgs = self.func.func_code.co_argcount
        minArgs = maxArgs - (len(self.func.func_defaults) if self.func.func_defaults else 0)

        args = string.split(None, maxArgs-1)[:maxArgs]
        if len(args) < minArgs:
            raise MagicError('Magic word %s requires at least %d arguments' % (self.name, minArgs))

        output = []
        for i, (type, arg) in enumerate(zip(self.types, args)):
            try:
                targ = type(arg)
            except (TypeError, ValueError):
                raise MagicError('Argument %d of magic word %s must be %s' % (i, self.name, type.__name__))

            output.append(targ)

        return output

    def run(self, rawArgs):
        args = self.parseArgs(rawArgs)
        return self.func(*args)

class MagicWordDecorator:
    """
    This class manages Magic Word decoration. It is aliased as magicWord, so that
    the @magicWord(...) construct instantiates this class and has the resulting
    object process the Magic Word's construction.
    """

    def __init__(self, category, types=[str], name=None):
        self.name = name
        self.types = types
        self.category = category
        self.access = self.category.access

    def __call__(self, mw):
        # This is the actual decoration routine. We add the function 'mw' as a
        # Magic Word to the Spellbook, using the attributes specified at construction
        # time.

        name = self.name
        if name is None:
            name = mw.func_name

        word = MagicWord(name, mw, self.types, self.access, mw.__doc__)
        spellbook.addWord(word)

        return mw

magicWord = MagicWordDecorator
