class ScrapterController:
    def __init__(self):
        self.ScrapterList = []

    def add_scrapter(self, Scrapter):
        self.ScrapterList.append(Scrapter)

    def delete_scrapter(self, Scrapter):
        self.ScrapterList.remove(Scrapter)

    def get_scrapter_list(self):
        return self.ScrapterList
