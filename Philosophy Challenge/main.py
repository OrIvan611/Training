from utils import *
from consts import *


used_urls = []
url = FIRST_URL
print(url)
for i in range(ITERATIONS):
    if url in used_urls:
        # We already visited this page.
        print('I am in a loop...')
        break
    used_urls.append(url)

    if check_if_title_match(url):
        # We found the requested ulr!
        print('i got it')
        break

    url = get_new_url(url)
    print(url)
    if not url:
        # The previous url had no valid links in it.
        print('There are no links in this page.')
        break
else:
    # We didn't find the requested url, and we got to the ITERATION limit.
    print(f'I tried {ITERATIONS} times..')

# Plot the graph without the random node.
plot_graph(used_urls[1:])




