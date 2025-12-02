from program.repository.BaseRepository import Repository as repo


class Report():

    def __init__(self, repo):
        self.repository = repo

    def unreadAmount():
        return repo.findByStatus("reading")
    
    def readingAmount():
        return repo.findByStatus("unread")
    
    def completedAmount():
        return repo.findByStatus("completed")

    def publicationAmount() -> int:
       return repo.findPublicationAmount()
    
    def completedAverageScore() -> float:
        scores = repo.findCompletedAverageScore()
        total = repo.findPublicationAmount()

        return (scores/total)

    def bestFive():
        return repo.findBestFivePublications()
        