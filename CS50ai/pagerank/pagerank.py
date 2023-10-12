import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            #?????????????????????????????????????????????????whats line 40
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    relevant_links = []
    for x in corpus[page]:
        relevant_links.append(x)
    dictionary_final = {}
    for links in relevant_links:
        dictionary_final[links] = damping_factor/len(relevant_links)+ 0.15/len(corpus)
    for y in corpus:
        if y in dictionary_final:
            continue
        else:
            dictionary_final[y] = 0.15/len(corpus)
    return dictionary_final

    """
    1)find the values of page inside the corpus and place them into a list
    2)create  a dictionary
    3)for each value in the corpus, calculate the probability of that value and
    place inside the dictionary--0.85divide by total number of values in corpus of that page
    4)then add on 0.15 divide by total number of pages(how to find len()of number
    of pages inside that corpus) it can go to.
    5)return that dictionary

    """
    """
    return a dictionary representing the probability distribution over which page a
    random surfer would visit next, given the following arguments

    page is a string representing which page a random surfer is currently on


    Return a dictionary of probability distribution over which page to visit next,
    given a current page. the total should sum to 1


    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """




def sample_pagerank(corpus, damping_factor, n):
    page_rank={}
    for x in corpus:
        page_rank[x]=0
    random_page = random.choice(list(corpus))
    page_rank[random_page] += 1

    for i in range(n-1):
        model = transition_model(corpus, random_page, damping_factor)
        pages, probability = zip(*model.items())
        random_page = random.choices(pages, probability)
        random_page="".join(random_page)
        page_rank[random_page]+=1
    for x in page_rank:
        page_rank[x]=page_rank[x]/n
    return page_rank



    """
    1) ranomdly choose one link from corpus
    2) create a loop over n
    2)
    uses sampling method

    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """


def iterate_pagerank(corpus, damping_factor):
    n=len(corpus)
    d=damping_factor
    ranks={}
    for page in corpus:
        ranks[page] =1/n
    change=1
    while change >=0.001:
        change=0
        dist=ranks.copy()
        for page in ranks:
            links=[link for link in corpus if page in corpus [link]]
            p1= (1-d)/n
            p2= []
            if len(links) !=0:
                for link in links:
                    num=len(corpus [link])
                    val=dist[link]/num
                    p2.append(val)
            summation = sum(p2)
            ranks[page]=p1+d*summation
            new =abs (ranks[page] -dist[page])
            if change < new:
                change = new
    return dist

''''
    page_rank = {}
    for x in corpus:
        page_rank[x] = 1/len(corpus)


#calculate the summation first for each page
    while True:
        for x in corpus: #our focus page(p)
            summation=0
            for y in corpus: #our other pages(i)
                if x in corpus[y]:
                    value=page_rank[y]/len(corpus[y])
                    summation+=value

            new_page_rank=round((1-damping_factor)/len(corpus)+damping_factor*summation, 3)
            if abs(new_page_rank-page_rank[x])>=0.001:
                page_rank[x] = new_page_rank
            else:
                return page_rank


'''





    #stop once value changes no more tha  0.001 between current rank values
    #and previous rank values. need find a way for loop to keep going




if __name__ == "__main__":
    main()
