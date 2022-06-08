from flask import Flask,jsonify,request
import csv 
allArticles=[]
with open("articles.csv")as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles=data[1:]
like_articles=[]
unlike_articles=[]
app=Flask(__name__)
@app.route("/get-articles")
def get_articles():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    })
@app.route("like-article",methods=['POST'])
def like_article():
    article=allArticles[0]
    all_articles=allArticles[1:]
    like_articles.append(article)
    return jsonify({
        "status":"success"
    }),201
@app.route("unlike-articles",methods=['POST'])
def unlike_articles():
    article=allArticles[0]
    all_articles=allArticles[1:]
    unlike_articles.append(article)
    return jsonify({
        "status":"success"
    }),201

if __name__=="__main__":
    app.run()
