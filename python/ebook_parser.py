"""

"""
from xml.dom.minidom import parseString
from bs4 import BeautifulSoup
from collections import Counter
from utils import dump
import re

"""


"""
class ebup_parser(object):
    
    """
    
    """
    def __init__(self, table_of_contents=None):
        self.folder_sep = '/'
        self.chapters = []
        self.num_chapters = 0
        self.current_chapter = 0
        self.toc_filepath = table_of_contents
        
        if self.toc_filepath is not None:
            # Split the parts
            fileparts = self.toc_filepath.split(self.folder_sep)
            
            # Create the dir name by getting all but the last parts
            # This assumes all files are relative
            self.dir = self.folder_sep.join(fileparts[:-1]) + self.folder_sep
        
        self.process_table_of_contents()
    
    
    """
        Process the table of contents to find the links to all the chapter
        files. We can later use this to get the contents for each chapter
    """        
    def process_table_of_contents(self):
        
        # Parse the first file's HTML with BS
        soup = BeautifulSoup(open(self.toc_filepath, 'r'), "lxml")

        # Get all the links and store them -> since this is the table of contents
        # the links contain the relative paths to the other chapters
        for link_ele in soup.find_all('a'):
        
            # The links contain anchor references, let's just ignore those
            file_location = link_ele.attrs['href'].split('#')[0]
            link_text = ''
            
            for a in link_ele.stripped_strings:
                link_text += a
                
            # Construct the link to the file
            file_location = self.dir + file_location
            
            # Store the info for this guy...
            self.chapters.append((link_text, file_location))
            self.num_chapters = len(self.chapters)   
    
    """
        Get Chapter Contents
    """
    def get_chapter_contents(self, chapter_num=None):
        body = ''
                
        if chapter_num is not None:
            self.current_chapter = chapter_num
            chapter_name, chapter_path = self.chapters[chapter_num]
            print('Reading Chapter %s - %s' % (chapter_num, chapter_name))
            
            # Open the file, parse it        
            document = BeautifulSoup(open(chapter_path, 'r'), "lxml")
            
            # Make sure we actually have a document here before trying to do anything else
            for string in document.body.strings:
                body = body + string
                #print string
            
            # Remove the title from the body
            body = body.replace(chapter_name.upper(), '')
            
        return body
             
    """
    
    """
    def get_next_chapter(self):
        self.current_chapter += 1
        
        if self.current_chapter < self.num_chapters:
            return self.chapters[self.current_chapter]
        else:
            return None
            

"""

"""
def remove_bad_words(word):
    ignored_words = [
        'all', 'the', 'and', 'him', 'his', 'did', 'but', 'she', 
        'you', 'was', 'not', 'that', 'with', 'for', 'had', 'will',
        'than', 'then', 'your', 'them', 'had', 'they', 'her', 'this',
        'were', 'its', 'will', 'said', 'are', 'their', 'there', 'told',
        'well', 'when', 'what', 'man', 'been'
    ]
     
    # If we have less than three chars, let's not count it
    if len(word) >= 3 and word not in ignored_words:
        return word 
    else:
        return False


"""

"""
def get_word_counter(textblob=''):
    word_counter = Counter('')
    
    if textblob:
        # Build regex to remove all non-alphanumeric characters
        reg = re.compile('\W')
        clean_text = reg.sub(' ', textblob.lower())
        
        # Convert to list, based on spaces
        words = clean_text.split(' ')
        
        # filter out any invalid / short words
        valid_words = filter(remove_bad_words, words)
        print 'Valid Words: %s' % len(valid_words)
        
        word_counter = Counter(valid_words)
    
    return word_counter
        
    
"""
    Sample: Instantiate this directly and call whatever you want
"""
if __name__ == "__main__":
    toc = 'C:/data/books/game_of_thrones/A_Game_Of_Thrones_split_001.html'
    
    book = ebup_parser(table_of_contents=toc)
    
    overall = Counter()
    
    for a in range(3, book.num_chapters):
        
        text = book.get_chapter_contents(a)
        current_chapter_words = get_word_counter(text)
        
        overall += current_chapter_words
    
    
    
    all_words = dict(overall.most_common(200))
    
    dump(all_words)
    

    
    
    
    