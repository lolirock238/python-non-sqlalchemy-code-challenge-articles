class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an Author object")

        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be a Magazine object")

        if isinstance(title, str):
            if 5 <= len(title) <= 50:
                 self._title = title
            else:
                raise ValueError("Title must be 5-50 characters")
        else:
            raise ValueError("Title must be a string")

        self.author = author
        self.magazine = magazine

        Article.all.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,value):
        pass


    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise ValueError("Author must be an Author object")
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise ValueError("Magazine must be a Magazine object")

        
class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        pass

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = [article.magazine.category for article in self.articles()]
        return list(set(topics)) if topics else None



class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        
        if isinstance(value, str):
            if 2 <= len(value) <= 16:
                self._name = value
           
        
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        
        if isinstance(value, str):
            if len(value) > 0:
                self._category = value
            

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None