class Author:
    def __init__(self, name):
        if isinstance(name, str):
            if len(name) > 0:
                self._name = name
            else:
                raise ValueError("Author name must be longer than 0 characters")
        else:
            raise ValueError("Author name must be a string")

    @property
    def name(self):
        return self._name

    def articles(self):
        # return all articles by this author
        result = []
        for article in Article.all:
            if article.author == self:
                result.append(article)
        return result

    def magazines(self):
        # return all magazines this author has written for (unique manually)
        mags = []
        for article in self.articles():
            if article.magazine not in mags:
                mags.append(article.magazine)
        return mags

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        cats = []
        for magazine in self.magazines():
            if magazine.category not in cats:
                cats.append(magazine.category)
        return cats


class Magazine:
    def __init__(self, name, category):
        if isinstance(name, str):
            if 2 <= len(name) <= 16:
                self._name = name
            else:
                raise ValueError("Magazine name must be 2–16 characters")
        else:
            raise ValueError("Magazine name must be a string")

        if isinstance(category, str):
            if len(category) > 0:
                self._category = category
            else:
                raise ValueError("Category must not be empty")
        else:
            raise ValueError("Category must be a string")

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        # all articles in this magazine
        result = []
        for article in Article.all:
            if article.magazine == self:
                result.append(article)
        return result

    def contributors(self):
        # authors who wrote for this magazine
        authors = []
        for article in self.articles():
            if article.author not in authors:
                authors.append(article.author)
        return authors

    def article_titles(self):
        # all article titles for this magazine
        titles = []
        for article in self.articles():
            titles.append(article.title)
        return titles

    def contributing_authors(self):
        # authors with more than 2 articles in this magazine
        authors = []
        for article in self.articles():
            authors.append(article.author)

        result = []
        for author in self.contributors():
            count = authors.count(author)
            if count > 2:
                result.append(author)
        return result


