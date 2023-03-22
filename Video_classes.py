class Video:

    def __init__(self, title, likes, views, link):
        self.__title = title
        self.__likes = likes
        self.__views = views
        self.__link = link

    def getTitle(self):
        return self.__title

    def getLikes(self):
        return self.__likes

    def getViews(self):
        return self.__views

    def getLink(self):
        return self.__link
