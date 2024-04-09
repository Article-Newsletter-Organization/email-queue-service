class MessageBody:
    def __init__(
        self,
        publicationId: str,
        articleId: str,
        subject: str,
        body: str,
        objectUrl: str,
        authorId: str,
    ):
        self.publicationId = publicationId
        self.articleId = articleId
        self.subject = subject
        self.body = body
        self.objectUrl = objectUrl
        self.authorId = authorId
