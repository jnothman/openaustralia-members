import openaustraliamembers
import scraperwiki


df = openaustraliamembers.OpenAustraliaMembers().offices().reset_index()
df.todate = df.todate.astype(str)
df.fromdate = df.fromdate.astype(str)
df['office_id_number'] = df.office_id.map(lambda s: int(s.rpartition('/')[-1]))
scraperwiki.sqlite.save(unique_keys=['office_id_number'],
                        data=df.to_dict(orient='records'))
