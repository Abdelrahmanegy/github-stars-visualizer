import requests 
#using plotly
from plotly.graph_objects import Bar 
from plotly import offline
def draw_graphs(language) :
    url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars"
    headers= {'Accept':'application/vnd.github.v3+json'}
    r= requests.get(url,headers=headers)
    print(f"statue code {r.status_code}")
    response_dict= r.json()
    repo_dicts=response_dict['items']
    repo_links,stars,labels=[],[],[]
    #loop through items and get the stars, names ,and links of the projects
    for repo_dict in repo_dicts:
        repo_name=repo_dict['name']
        repo_url=repo_dict['html_url']
        repo_link=f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)
        stars.append(repo_dict['stargazers_count'])
        owner=repo_dict['owner']['login']
        description=repo_dict['description']
        label=f"{owner}<br />{description}"
        labels.append(label)
    #make visualizations 
    data=[
  {
    'type':'bar',
    'x'   : repo_links,
    'y'   : stars,
    'hovertext':labels
    #'marker':{
     # 'color':'rgb(60,100,150)',
     # 'line' : {'width':1.5,'color':'rgb(25,25,25)'}
    #},
    #'opacity':0.6,
  }
]
    my_layout={
  'title' : f'Most starred {language} projects on github',
  'xaxis' : {'title':'Repositry',
             'titlefont':{'size':24},
             'tickfont' :{'size':14}
             },
  'yaxis'  : {'title': 'Stars',
              'titlefont':{'size':24},
              'tickfont' :{'size':14}
              }
  
}
    fig= {'data':data, 'layout':my_layout}  
    offline.plot(fig,filename='starred_project.html') 
