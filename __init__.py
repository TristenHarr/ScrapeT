def go(search_for=["python"],search_type='track', limit=60, limit_type='time', table_name='Scraper', database_name='Twitter', lang=None, location_geo_box_lookup=None):
    item = open("InRoute/limit.txt", 'w')
    item.write("{} {}".format(limit, limit_type.upper()))
    item.close()
    from ScrapeData import tagger
    track = tagger.track
    locate = tagger.location
    lookup = tagger.loc_lookup
    if search_type == 'track':
        if lang != None:
            track(search_for, languages=lang)
        else:
            track(search_for)
    elif search_type == 'location':
        if lang != None:
            if location_geo_box_lookup != None:
                locate(lookup(location_geo_box_lookup), languages=lang)
            else:
                locate(search_for, languages=lang)
        else:
            if location_geo_box_lookup != None:
                locate(lookup(location_geo_box_lookup))
            else:
                locate(search_for)
    from ScrapeData.InRoute.DeepStore import store_it
    store_it(table_name, database_name)

go(location_geo_box_lookup="US", search_type='location', limit_type="COUNT", limit=1000, lang=['en'])
