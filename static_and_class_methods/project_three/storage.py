from project_three.category import Category
from project_three.document import Document
from project_three.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []
    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)
    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = [category for category in self.categories if category.id == category_id][0]
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [topic for topic in self.topics if topic.id == topic_id][0]
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = [document for document in self.documents if document.id == document_id][0]
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = [category for category in self.categories if category.id == category_id][0]
        self.categories.remove(category)
    def delete_topic(self, topic_id):
        topic = [topic for topic in self.topics if topic.id == topic_id][0]
        self.topics.remove(topic)
    def delete_document(self, document_id):
        document = [document for document in self.documents if document.id == document_id][0]
        self.documents.remove(document)
    def get_document(self, document_id):
        document = [document for document in self.documents if document.id == document_id]
        return document

    def __repr__(self):
        result = []
        for doc in self.documents:
            result.append(repr(doc))
        return '\n'.join(result)


c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project_three")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)





