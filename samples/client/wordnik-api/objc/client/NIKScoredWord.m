#import "NIKDate.h"
#import "NIKScoredWord.h"

@implementation NIKScoredWord

@synthesize _id = __id;
@synthesize position = _position;
@synthesize lemma = _lemma;
@synthesize docTermCount = _docTermCount;
@synthesize wordType = _wordType;
@synthesize score = _score;
@synthesize word = _word;
@synthesize sentenceId = _sentenceId;
@synthesize stopword = _stopword;
@synthesize baseWordScore = _baseWordScore;
@synthesize partOfSpeech = _partOfSpeech;
- (id) _id: (NSNumber*) _id
       position: (NSNumber*) position
       lemma: (NSString*) lemma
       docTermCount: (NSNumber*) docTermCount
       wordType: (NSString*) wordType
       score: (NSNumber*) score
       word: (NSString*) word
       sentenceId: (NSNumber*) sentenceId
       stopword: (NSNumber*) stopword
       baseWordScore: (NSNumber*) baseWordScore
       partOfSpeech: (NSString*) partOfSpeech
       {
          __id = _id;
          _position = position;
          _lemma = lemma;
          _docTermCount = docTermCount;
          _wordType = wordType;
          _score = score;
          _word = word;
          _sentenceId = sentenceId;
          _stopword = stopword;
          _baseWordScore = baseWordScore;
          _partOfSpeech = partOfSpeech;
          return self;
       }

- (id) initWithValues: (NSDictionary*)dict
{
    /* isContainer: , baseType: NSNumber, complexType:  */
    __id = [dict objectForKey:@"id"];
    /* isContainer: , baseType: NSNumber, complexType:  */
    _position = [dict objectForKey:@"position"];
    /* isContainer: , baseType: NSString, complexType:  */
    _lemma = [dict objectForKey:@"lemma"];
    /* isContainer: , baseType: NSNumber, complexType:  */
    _docTermCount = [dict objectForKey:@"docTermCount"];
    /* isContainer: , baseType: NSString, complexType:  */
    _wordType = [dict objectForKey:@"wordType"];
    /* isContainer: , baseType: NSNumber, complexType:  */
    _score = [dict objectForKey:@"score"];
    /* isContainer: , baseType: NSString, complexType:  */
    _word = [dict objectForKey:@"word"];
    /* isContainer: , baseType: NSNumber, complexType:  */
    _sentenceId = [dict objectForKey:@"sentenceId"];
    /* isContainer: , baseType: NSNumber, complexType:  */
    _stopword = [dict objectForKey:@"stopword"];
    /* isContainer: , baseType: NSNumber, complexType:  */
    _baseWordScore = [dict objectForKey:@"baseWordScore"];
    /* isContainer: , baseType: NSString, complexType:  */
    _partOfSpeech = [dict objectForKey:@"partOfSpeech"];
    return self;
}

-(NSDictionary*) asDictionary {
    NSMutableDictionary* dict = [[NSMutableDictionary alloc] init];
    if(__id != nil) [dict setObject:__id forKey:@"id"];
    if(_position != nil) [dict setObject:_position forKey:@"position"];
    if(_lemma != nil) [dict setObject:_lemma forKey:@"lemma"];
    if(_docTermCount != nil) [dict setObject:_docTermCount forKey:@"docTermCount"];
    if(_wordType != nil) [dict setObject:_wordType forKey:@"wordType"];
    if(_score != nil) [dict setObject:_score forKey:@"score"];
    if(_word != nil) [dict setObject:_word forKey:@"word"];
    if(_sentenceId != nil) [dict setObject:_sentenceId forKey:@"sentenceId"];
    if(_stopword != nil) [dict setObject:_stopword forKey:@"stopword"];
    if(_baseWordScore != nil) [dict setObject:_baseWordScore forKey:@"baseWordScore"];
    if(_partOfSpeech != nil) [dict setObject:_partOfSpeech forKey:@"partOfSpeech"];
    NSDictionary* output = [dict copy];
    return output;
}

@end

