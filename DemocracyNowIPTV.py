import xml.etree.ElementTree
import urllib2

feed_url = "https://www.democracynow.org/podcast-video.xml"
namespaces = {'media': 'http://search.yahoo.com/mrss/'}

response = urllib2.urlopen(feed_url)
xml_feed = response.read()
e = xml.etree.ElementTree.fromstring(xml_feed)

print('#EXTM3U')

for channel in e.findall('channel'):
        #print channel.tag
        for atem in channel.findall('item'):
                mediac = atem.find('media:content', namespaces)
                thumbnail = atem.find('media:thumbnail', namespaces)
                print('#EXTINF:{0} tvg-logo="{1}", {2}').format(
                                mediac.get('duration'),
                                thumbnail.get('url'),
                                atem.find('title').text);
                print(mediac.get('url'))
