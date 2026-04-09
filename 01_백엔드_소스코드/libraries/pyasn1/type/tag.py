# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tag.pyc (Python 3.11)

from pyasn1 import error
__all__ = [
    'tagClassUniversal',
    'tagClassApplication',
    'tagClassContext',
    'tagClassPrivate',
    'tagFormatSimple',
    'tagFormatConstructed',
    'tagCategoryImplicit',
    'tagCategoryExplicit',
    'tagCategoryUntagged',
    'Tag',
    'TagSet']
tagClassUniversal = 0
tagClassApplication = 64
tagClassContext = 128
tagClassPrivate = 192
tagFormatSimple = 0
tagFormatConstructed = 32
tagCategoryImplicit = 1
tagCategoryExplicit = 2
tagCategoryUntagged = 4

class Tag(object):
    '''Create ASN.1 tag

    Represents ASN.1 tag that can be attached to a ASN.1 type to make
    types distinguishable from each other.

    *Tag* objects are immutable and duck-type Python :class:`tuple` objects
    holding three integer components of a tag.

    Parameters
    ----------
    tagClass: :py:class:`int`
        Tag *class* value

    tagFormat: :py:class:`int`
        Tag *format* value

    tagId: :py:class:`int`
        Tag ID value
    '''
    
    def __init__(self, tagClass, tagFormat, tagId):
        if tagId < 0:
            raise error.PyAsn1Error('Negative tag ID (%s) not allowed' % tagId)
        self._Tag__tagClass = tagClass
        self._Tag__tagFormat = tagFormat
        self._Tag__tagId = tagId
        self._Tag__tagClassId = (tagClass, tagId)
        self._Tag__hash = hash(self._Tag__tagClassId)

    
    def __repr__(self):
        representation = f'''[{self._Tag__tagClass!s}:{self._Tag__tagFormat!s}:{self._Tag__tagId!s}]'''
        return f'''<{self.__class__.__name__!s} object, tag {representation!s}>'''

    
    def __eq__(self, other):
        return self._Tag__tagClassId == other

    
    def __ne__(self, other):
        return self._Tag__tagClassId != other

    
    def __lt__(self, other):
        return self._Tag__tagClassId < other

    
    def __le__(self, other):
        return self._Tag__tagClassId <= other

    
    def __gt__(self, other):
        return self._Tag__tagClassId > other

    
    def __ge__(self, other):
        return self._Tag__tagClassId >= other

    
    def __hash__(self):
        return self._Tag__hash

    
    def __getitem__(self, idx):
        if idx == 0:
            return self._Tag__tagClass
        if None == 1:
            return self._Tag__tagFormat
        if None == 2:
            return self._Tag__tagId
        raise None

    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __and__(self, otherTag):
        return self.__class__(self._Tag__tagClass & otherTag.tagClass, self._Tag__tagFormat & otherTag.tagFormat, self._Tag__tagId & otherTag.tagId)

    
    def __or__(self, otherTag):
        return self.__class__(self._Tag__tagClass | otherTag.tagClass, self._Tag__tagFormat | otherTag.tagFormat, self._Tag__tagId | otherTag.tagId)

    tagClass = (lambda self: self._Tag__tagClass)()
    tagFormat = (lambda self: self._Tag__tagFormat)()
    tagId = (lambda self: self._Tag__tagId)()


class TagSet(object):
    """Create a collection of ASN.1 tags

    Represents a combination of :class:`~pyasn1.type.tag.Tag` objects
    that can be attached to a ASN.1 type to make types distinguishable
    from each other.

    *TagSet* objects are immutable and duck-type Python :class:`tuple` objects
    holding arbitrary number of :class:`~pyasn1.type.tag.Tag` objects.

    Parameters
    ----------
    baseTag: :class:`~pyasn1.type.tag.Tag`
        Base *Tag* object. This tag survives IMPLICIT tagging.

    *superTags: :class:`~pyasn1.type.tag.Tag`
        Additional *Tag* objects taking part in subtyping.

    Examples
    --------
    .. code-block:: python

        class OrderNumber(NumericString):
            '''
            ASN.1 specification

            Order-number ::=
                [APPLICATION 5] IMPLICIT NumericString
            '''
            tagSet = NumericString.tagSet.tagImplicitly(
                Tag(tagClassApplication, tagFormatSimple, 5)
            )

        orderNumber = OrderNumber('1234')
    """
    
    def __init__(self, baseTag = ((),), *superTags):
        self._TagSet__baseTag = baseTag
        self._TagSet__superTags = superTags
        self._TagSet__superTagsClassId = (lambda .0: [ (superTag.tagClass, superTag.tagId) for superTag in .0 ])(superTags())
        self._TagSet__lenOfSuperTags = len(superTags)
        self._TagSet__hash = hash(self._TagSet__superTagsClassId)

    
    def __repr__(self):
        representation = (lambda .0: [ f'''{x.tagClass!s}:{x.tagFormat!s}:{x.tagId!s}''' for x in .0 ])(self._TagSet__superTags())
        return f'''<{self.__class__.__name__!s} object, {representation!s}>'''

    
    def __add__(self, superTag):
        pass
    # WARNING: Decompyle incomplete

    
    def __radd__(self, superTag):
        pass
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, i):
        pass
    # WARNING: Decompyle incomplete

    
    def __eq__(self, other):
        return self._TagSet__superTagsClassId == other

    
    def __ne__(self, other):
        return self._TagSet__superTagsClassId != other

    
    def __lt__(self, other):
        return self._TagSet__superTagsClassId < other

    
    def __le__(self, other):
        return self._TagSet__superTagsClassId <= other

    
    def __gt__(self, other):
        return self._TagSet__superTagsClassId > other

    
    def __ge__(self, other):
        return self._TagSet__superTagsClassId >= other

    
    def __hash__(self):
        return self._TagSet__hash

    
    def __len__(self):
        return self._TagSet__lenOfSuperTags

    baseTag = (lambda self: self._TagSet__baseTag)()
    superTags = (lambda self: self._TagSet__superTags)()
    
    def tagExplicitly(self, superTag):
        '''Return explicitly tagged *TagSet*

        Create a new *TagSet* representing callee *TagSet* explicitly tagged
        with passed tag(s). With explicit tagging mode, new tags are appended
        to existing tag(s).

        Parameters
        ----------
        superTag: :class:`~pyasn1.type.tag.Tag`
            *Tag* object to tag this *TagSet*

        Returns
        -------
        : :class:`~pyasn1.type.tag.TagSet`
            New *TagSet* object
        '''
        if superTag.tagClass == tagClassUniversal:
            raise error.PyAsn1Error("Can't tag with UNIVERSAL class tag")
        if superTag.tagFormat != tagFormatConstructed:
            superTag = Tag(superTag.tagClass, tagFormatConstructed, superTag.tagId)
        return self + superTag

    
    def tagImplicitly(self, superTag):
        '''Return implicitly tagged *TagSet*

        Create a new *TagSet* representing callee *TagSet* implicitly tagged
        with passed tag(s). With implicit tagging mode, new tag(s) replace the
        last existing tag.

        Parameters
        ----------
        superTag: :class:`~pyasn1.type.tag.Tag`
            *Tag* object to tag this *TagSet*

        Returns
        -------
        : :class:`~pyasn1.type.tag.TagSet`
            New *TagSet* object
        '''
        if self._TagSet__superTags:
            superTag = Tag(superTag.tagClass, self._TagSet__superTags[-1].tagFormat, superTag.tagId)
        return self[:-1] + superTag

    
    def isSuperTagSetOf(self, tagSet):
        '''Test type relationship against given *TagSet*

        The callee is considered to be a supertype of given *TagSet*
        tag-wise if all tags in *TagSet* are present in the callee and
        they are in the same order.

        Parameters
        ----------
        tagSet: :class:`~pyasn1.type.tag.TagSet`
            *TagSet* object to evaluate against the callee

        Returns
        -------
        : :py:class:`bool`
            :obj:`True` if callee is a supertype of *tagSet*
        '''
        if len(tagSet) < self._TagSet__lenOfSuperTags:
            return False
        return None._TagSet__superTags == tagSet[:self._TagSet__lenOfSuperTags]

    
    def getBaseTag(self):
        return self._TagSet__baseTag



def initTagSet(tag):
    return TagSet(tag, tag)
