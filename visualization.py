import util

def table_show(univ):
    c1 = ['Name','Country','Region','Foundation Year','Student Number','Faculty Number',
    'Student/Faculty Ratio','Location','Country Ranking','World Ranking','Teaching Ranking',
    'Research Ranking','International Diversity Ranking','Financial Ranking','Description',
    'Website','Address']
    c2 = []
    for i in univ:
        c2.append(univ[i])
    c2.pop()
    c = [c1,c2]
    header = {}
    header['values'] = []
    dict = {}
    dict['values'] = c
    dict['line_color'] = 'darkslategray'
    dict['font_size'] = 13
    dict['height'] = 32
    fig = util.plotly.graph_objects.Figure(
        data=[
            util.plotly.graph_objects.Table(
                columnorder = [1,2],
                columnwidth = [120,400],
                header = header,
                cells=dict)
            ]
    )
    fig.show()
def pie_show(univ):
    labels = ['Student','Faculty']
    values = [univ['stud'],univ['fac']]
    tr = util.plotly.graph_objects.Pie(labels=labels, values=values)

    return tr
def bar_show(univ):
    x = ['Country Ranking','World Ranking','Teaching Ranking',
    'Research Ranking','International Diversity Ranking','Financial Ranking']
    y = [1000-int(univ["O_CR"]),1000-int(univ["O_WR"]),1000-int(univ["O_TR"]),1000-int(univ["O_RR"]),1000-int(univ["O_IR"]),1000-int(univ["O_FR"])]
    for i in range(len(y)):
        y[i] = y[i] /1000 * 100
    y1 = [int(univ["O_CR"]),int(univ["O_WR"]),int(univ["O_TR"]),int(univ["O_RR"]),int(univ["O_IR"]),int(univ["O_FR"])]
    tr = util.plotly.graph_objects.Bar(
                x=x,y=y,
                text = y1,
                textposition='auto',
            )

    #fig2.update_yaxes(showticklabels=False)
    return tr
def map_show(univ):
    geolocator = util.Nominatim(user_agent="http")  
    try:        
        location = geolocator.geocode(univ['addr'])   
        d = {'lat':[location.latitude],'lon':[location.longitude]}
        df = util.pd.DataFrame(data=d)
        fig3 = util.px.scatter_mapbox(df, lat="lat", lon="lon", 
                            color_discrete_sequence=["fuchsia"], zoom=3, height=600)
        fig3.update_layout(mapbox_style="open-street-map")
        fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        return fig3
    except:
        try:
            addr = univ['addr'][univ['addr'].find(',') + 1:]
            location = geolocator.geocode(addr)   
            d = {'lat':[location.latitude],'lon':[location.longitude]}
            df = util.pd.DataFrame(data=d)
            fig3 = util.px.scatter_mapbox(df, lat="lat", lon="lon", 
                                color_discrete_sequence=["fuchsia"], zoom=3, height=600)
            fig3.update_layout(mapbox_style="open-street-map")
            fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            return fig3
        except:
            try:
                addr = univ['addr'][univ['addr'].find(',',univ['addr'].find(',')  + 1) + 1:]
                location = geolocator.geocode(addr)   
                d = {'lat':[location.latitude],'lon':[location.longitude]}
                df = util.pd.DataFrame(data=d)
                fig3 = util.px.scatter_mapbox(df, lat="lat", lon="lon", 
                                    color_discrete_sequence=["fuchsia"], zoom=3, height=600)
                fig3.update_layout(mapbox_style="open-street-map")
                fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                return fig3
            except:
                try:
                    addr = univ['loc']
                    location = geolocator.geocode(addr)   
                    d = {'lat':[location.latitude],'lon':[location.longitude]}
                    df = util.pd.DataFrame(data=d)
                    fig3 = util.px.scatter_mapbox(df, lat="lat", lon="lon", 
                                        color_discrete_sequence=["fuchsia"], zoom=3, height=600)
                    fig3.update_layout(mapbox_style="open-street-map")
                    fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                    return fig3
                except:
                    return -1
def table_show1(univ):
    c1 = ['Name','Country','Region','Foundation Year','Description','Website']
    c2 = []
    num = 0
    for i in univ:
        if num == 0 or num == 1 or num == 2 or num == 3 or num == 14 or num == 15:
            c2.append(univ[i])
        num += 1
    c2.append(univ['website'])
    c2.pop()
    c = [c1,c2]
    header = {}
    header['values'] = ['']
    dict = {}
    dict['values'] = c
    dict['line_color'] = 'darkslategray'
    dict['font_size'] = 13
    dict['height'] = 32
    tr = util.plotly.graph_objects.Table(
                header = header,
                cells=dict)
    return tr
def show1(univ):
    fig = util.make_subplots(
    rows=1, cols=3, shared_xaxes=True, 
    vertical_spacing=0.02,specs=[[{"type": "table"},{"type": "pie"},{"type": "bar"}]],
           subplot_titles=("Basic Information", "Student/Faculty Ratio","University Ranking"))

    fig.add_trace(table_show1(univ),
            row=1, col=1)

    fig.add_trace(pie_show(univ),row=1, col=2)

    fig.add_trace(bar_show(univ),row=1, col=3)

    fig.update_layout(height=600, width=1400,
                title_text="University Information")
    fig.update_yaxes(showticklabels=False)
    with open('p_graph.html', 'w') as f:
        f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write('<p>University Location</p>')
        if map_show(univ) != -1:
            f.write(map_show(univ).to_html(full_html=False, include_plotlyjs='cdn'))
        else:
            f.write('Sorry, no available data.')
    util.webbrowser.open_new_tab('p_graph.html')