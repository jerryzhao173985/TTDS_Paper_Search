from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
from .models import Paper
# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        # url = 'https://www.ask.com/web?q='+search
        # res = requests.get(url)
        # soup = bs(res.text, 'lxml')

        # result_listings = soup.find_all('div', {'class': 'PartialSearchResults-item'})
        
        final_result = []
        
        all_papers_list = Paper.objects.all()
        for paper in all_papers_list:
            if search in paper.title:
                if paper.url!="None":
                    final_result.append((paper.title, paper.url, paper.abstract))
                else:
                    search1 = "+".join(paper.title.split())
                    # print(search1)
                    url = 'https://google.com/search?q='+search1
                    # res = requests.get(url)
                    # soup = bs(res.text, 'lxml')
                    # # Creating soup from the fetched request
                    # # soup = bs(res.text, "html.parser")
                    
                    # # result_listings = soup.find_all('div', {'class': "h3"})
                    # # primal_result = result_listings[0]
                    # # # result_title = result.find(class_='PartialSearchResults-item-title').text
                    # # result_url = primal_result.find('a').get('href')
                    # # result_desc = result.find(class_='PartialSearchResults-item-abstract').text
                    
                    # first_link = soup.select_one('.yuRUbf').get('href')
                    # print(first_link)

                    final_result.append((paper.title, url, paper.abstract))

        
        # for result in result_listings:
        #     result_title = result.find(class_='PartialSearchResults-item-title').text
        #     result_url = result.find('a').get('href')
        #     result_desc = result.find(class_='PartialSearchResults-item-abstract').text

        #     final_result.append((result_title, result_url, result_desc))

        context = {
            'final_result': final_result
        }

        return render(request, 'search.html', context)

    else:
        return render(request, 'search.html')