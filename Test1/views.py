from django.shortcuts import render, redirect
from django.contrib import auth
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

l1=[]
global fg
l2=[]

rs1=[]

rs2=[]

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def FirstAdd(request):
    dict1={}
    name=request.POST.get("Player Name")
    team=request.POST.get("Player Team")
    turn=request.POST.get("Player Turn")
    rank=request.POST.get("Rank")
    score=request.POST.get("Score")
    sixer=request.POST.get("Player Sixer")
    four=request.POST.get("Player Four")
    dict1.update({"name":name,"team":team,"turn":turn,"rank":rank,"score":score,"sixer":sixer, "four":four})
    l1.append(dict1)
    return Response("Added First Team SuccessFully")
   

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def SecondAdd(request):
    
    dict2={}
    name1=request.POST.get("Player Name")
    team1=request.POST.get("Player Team")
    turn1=request.POST.get("Player Turn")
    rank1=request.POST.get("Rank")
    over=request.POST.get("Over")
    wickets=request.POST.get("Wickets")
    wicketname=request.POST.get("Wicket Name")
    dict2.update({"name":name1,"team":team1,"turn":turn1,"rank":rank1,"over":over,"wickets":wickets, "wicketname":wicketname})
    l2.append(dict2)
    if int(over) <= 5:
        return Response("Added Second Team SuccessFully")
    else:
        return Response("5 Overs Completed")
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def FirstView(request):
    ts1=0
    tr1=0
    tsix1=0
    tf1=0
    for i in range(len(l1)):
        ts1= ts1+int(l1[i]["score"])
        tr1=tr1+int(l1[i]["rank"])
        tsix1=tsix1+int(l1[i]["sixer"])
        tf1=tf1+int(l1[i]["four"])
    r1={"Total Score":ts1,"Total rank":tr1,"Total sixer":tsix1,"Total Four":tf1}
    rs1.append(r1)
    global fg
    fg=rs1
    return Response(l1+rs1) 


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def SecondView(request):
    to2=0
    tw2=0
    tr2=0
    for i in range(len(l2)):
        to2= to2+int(l2[i]["over"])
        tw2=tw2+int(l2[i]["wickets"])
        tr2=tr2+int(l2[i]["over"])
    r2={"Total Over":to2,"Total Rank":tr2,"Total wickets":tw2}
    rs2.append(r2)
    print(fg)
    print(rs2)
    if int(rs1[0]["Total rank"]) > int(rs2[0]["Total Rank"]):
        b={"FirstTeam(Winner)":l1+rs1,"SecondTeam":l2+rs2}
    else:
        b={"SecondTeam(Winner)":l2+rs2,"FirstTeam":l1+rs1}
    return Response(b)

        
    