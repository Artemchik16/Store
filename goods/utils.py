from django.contrib.postgres.search import (
    SearchHeadline,
    SearchQuery,
    SearchRank,
    SearchVector,
)

from goods.models import Products


def get_search_queryset(search_query: str):
    vector = SearchVector("name", "description")
    query = SearchQuery(search_query)

    if search_query.isdigit() and len(search_query) <= 5:
        return Products.objects.filter(id=int(search_query))

    result = (
        Products.objects.annotate(rank=SearchRank(vector, search_query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )
    result = result.annotate(
        name_headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )

    # result = result.annotate(
    #     description_headline=SearchHeadline(
    #         "description",
    #         query,
    #         start_sel='<span style="background-color: yellow;">',
    #         stop_sel="</span>",
    #     )
    # )

    return result
