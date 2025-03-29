from sites.models import Article
def run():
    for i in range(5,15):
        article=Article()
        article.title="Arcticle N° #%d" % i
        article.desc="Description article N° #%d" % i
        article.image="http://default"
        article.save()
print("operation reussie")