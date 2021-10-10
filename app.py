from api import api, app
from api.resources.author import AuthorResource, AuthorListResource
from api.resources.quote import QuoteResource, QuoteListResource, \
    QuotesByAuthorsResource, QuotesChangeRateResource, \
    QuoteListSortedIdResource, QuoteListSortedAuthorNameResource


api.add_resource(AuthorListResource, "/author")
api.add_resource(AuthorResource, "/author/<int:id>", "/author")

api.add_resource(QuoteListResource, "/quotes")
api.add_resource(QuoteResource, "/quotes", "/author/<int:author_id>/quotes")
# Изменение рейтинга цитате dec/inc
api.add_resource(QuotesChangeRateResource, "/quotes/<int:quote_id>/<type>")
api.add_resource(QuotesByAuthorsResource, "/author/<int:author_id>/quotes/<int:quote_id>")

api.add_resource(QuoteListSortedIdResource, "/quotes/idsorted")  # Все цитаты c сортировкой по id
api.add_resource(QuoteListSortedAuthorNameResource, "/quotes/authornamesorted")  # Все цитаты c сортировкой по имени автора

if __name__ == '__main__':
    app.run(debug=True)
