# -*- coding: utf-8 -*-
from .processing import do_sum, QC_Sim1, QC_Sim3
from rq import Queue
from .worker import conn
from .utils import count_words_at_url
import pprint
# A very simple Flask Hello World app for you to get started with...
#<p>+: {result.plus}/{result.total}</p>
#<p>-: {result.minus}/{result.total}</p>
from flask import Flask, request
#result_new1 = QC_Sim1()
#result_new3 = [QC_Sim3(1),QC_Sim3(2),QC_Sim3(3),QC_Sim3(4)]
q = Queue(connection=conn)

app = Flask(__name__)
app.config["DEBUG"]=True
#app.config["UPLOAD_FOLDER"]="/home/prannerta100/mysite/"

@app.route('/', methods=["GET", "POST"])
#def hello_world():
#    return 'Hello from Flask!'
def adder_page():
    errors = ""

    if request.method == "POST":
        #dummy_queue = q.enqueue(count_words_at_url, 'http://heroku.com')
        ff = request.form.to_dict().keys()
        if 'task1' in ff:
            #job_q = q.enqueue(QC_Sim1)
            result = QC_Sim1()
            return '''
                    <html>
                        <body>
                            <p> -: {result1}/{tot} बार  </p>
                            <p> +: {result2}/{tot} बार   </p>
                            <p><a href="/"> मुख्य पृष्ठ पर वापस जाएँ</a></p>
                        </body>
                    </html>
                '''.format(result1=result['0'], result2=result['1'],tot=result['0']+result['1'])
        if 'task2' in ff:
            if request.form["choice"] == None:
                choice = 1
            else:
                choice = int(request.form["choice"])
                if(choice < 1):
                    choice = 1


            if choice in [3,4]:
                corr = "स्थिर (constant)"
            else:
                corr = "संतुलित (balanced)"

            ans = QC_Sim3(choice)
            #ans = q.enqueue(QC_Sim3,choice)
            if ans == "constant":
                ansn = "स्थिर (constant)"
            else:
                ansn = "संतुलित (balanced)"
            return '''
                    <html>
                        <body>
                            <p> सही/अपेक्षित जवाब:   </p>
                            <p> {corrstr} </p>
                            <p> IBM क्वांटम संगणक का जवाब:</p>
                            <p>  {ansnstr} </p>
                            <p><a href="/"> मुख्य पृष्ठ पर वापस जाएँ</a></p>
                        </body>
                    </html>
                '''.format(corrstr=corr,ansnstr=ansn)
    return '''
    <!DOCTYPE html>
<html lang="hi" xml:lang="hi" xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Quantum Horoscope</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <style>
    /* Remove the navbar's default margin-bottom and rounded borders */
    .navbar {
      margin-bottom: 0;
      border-radius: 0;
    }

    /* Set height of the grid so .sidenav can be 100% (adjust as needed) */
    .row.content {height: 450px}

    /* Set gray background color and 100% height */
    .sidenav {
      padding-top: 20px;
      background-color: #f1f1f1;
      height: 100%;
    }


    /* Set black background color, white text and some padding */
    footer {
      background-color: #555;
      color: white;
      padding: 15px;
    }

    /* On small screens, set height to 'auto' for sidenav and grid */
    @media screen and (max-width: 767px) {
      .sidenav {
        height: auto;
        padding: 15px;
      }
      .row.content {height:auto;}
    }
  </style>
</head>
<body>
<div class="container-fluid text-center">
  <div class="row content">
    <div class="col-sm-2 sidenav fullscreen">
      <div class="well">
        <a href="https://hi.wikipedia.org/wiki/%E0%A4%95%E0%A5%8D%E0%A4%B5%E0%A4%BE%E0%A4%A3%E0%A5%8D%E0%A4%9F%E0%A4%AE_%E0%A4%95%E0%A4%AE%E0%A5%8D%E0%A4%AA%E0%A5%8D%E0%A4%AF%E0%A5%82%E0%A4%9F%E0%A4%B0">Quantum Computing (क्वांटम संगणन)</a>
        </div>
      <div class="well">
        <a href="https://www.qiskit.org">IBM Qiskit</a>
        </div>
      <figure>
      <img width=75% class="center-block" src="static/qiskit_logo.jpg">
      </figure>
      <hr>
      <div class="well">
        <a href="https://github.com/prannerta100/quantum-horoscope">Github (गिटहब)</a>
        </div>
    </div>
    <div class="col-sm-8 text-left">
      <h1 class="text-center">Welcome to "quantum horoscope!"</h1>
      <h1 class="text-center">"क्वांटम कुंडली" पर आपका हार्दिक स्वागत है!</h1>
      <h2 class="text-center">You can access IBM's Quantum Cloud and play with real quantum computers without the need to learn any programming!</h2>
      <p> इस माध्यम के द्वारा मैं आपको एक मज़ेदार तरीके से क्वांटम संगणन के बारे में जानने व उसके साथ खेलने (सौजन्य आई.बी.एम.) का अवसर देना चाहूंगा।  दोस्तों क्वांटम संगणन एक अजूबा है। यदि आप प्रौद्योगोकी के क्षेत्र से हैं तो आपको "मूर सिद्धांत" के बारे में पता ही होगा। पिछले तीन दशकों में करीबन हर दो सालों में संगणन चिपों का कद आधा होता चला जा रहा है। परंतु यह दौर अब बरकरार नहीं रह सकता, क्योंकि हमारे ट्रांसिस्टिर अब बेहद जटिल होते होते कुछ अणुओं के कद को छूने की कगार पर हैं, हालाँकि हमारी संगणनीय ज़रूरतें बढ़ती चली जा रही हैं। ऐसे में संगणन के क्षेत्र का वर्चस्व बनाये रखने के लिए हमें नए तौर-तरीके अपनाने होंगे। </p>
      <p> इसवी सन् 1983 में भौतिकवैज्ञानिक रिचर्ड फेनमैन ने क्वांटम संगणन के बारे में आशा व्यक्त की थी। सूक्ष्म पदार्थ न्यूटन के सिद्धांतों का पालन नहीं करते। बल्कि वे क्वांटम सिद्धांतों से चलते हैं। वे किसी भी समय में दो अलग लक्षणों के रैखिक जोड़ में रह सकते हैं। इसे दर्शाने के लिए स्च्रोडिंगेर की क्वांटम बिल्ली का उदहारण दिया जाता है। सूक्ष्म पदार्थ एक क्वांटम बिल्ली की तरह हैं, जो किसी एक समय में जिवंत और मृत दोनों अवस्थाओं में रह सकती है। </p>
      <p> परन्तु इसका संगणन से क्या लेना देना? जब आप दो लक्षणवाले (मान लीजिये + और -) तीन  पदार्थों को लेते हैं तो आप उनको 2+2+2=6 परिमाणों में उनका सामूहिक वर्णन करते हैं।  परन्तु क्वांटम पदार्थ एक दूसरे से भिड़ सकते हैं - यानी आपके पास अब 2x2x2=8 परिमाण आ जाते हैं। योग के बदले गुणन - यही क्वांटम पदार्थों के द्वारा किये गए संगणन के पीछे का राज़ है। गुणन से आपके परिमाण बढ़ते जाते हैं। इतने ज़्यादा कि महज़ 53 क्वांटम पदार्थों से आप दुनिया के सबसे शक्तिशाली संगणक "समिट" के छक्के छुड़वा सकते हैं। क्योंकि 2x2x...x2 53 बार करने से जवाब करीबन एक करोड़ अबज (10<sup>16</sup>) आता है!</p>

      <figure>
      <!-- div class="span4"><img class="center-block" src="logo.png" /></div> -->
          <img class="center-block" src="static/scat.jpg" alt="Schrodinger's cat" style="width:50%">
          <figcaption><h4 class="text-center">स्च्रोडिंगेर की क्वांटम बिल्ली, जो जिवंत और मृत दोनों अवस्था में रह सकती है।</h4></figcaption>
      </figure>
      <p> क्वांटम संगणन के क्षेत्र में आये दिन नए आविष्कार होते चले आ रहे हैं। हाल ही में गूगल ने क्वांटम श्रेष्ठता (quantum supremacy) की घोषणा की। अधिक जानकारी के लिए <a href="https://ai.googleblog.com/2019/10/quantum-supremacy-using-programmable.html">यहाँ </a> जाएँ। संक्षेप में क्वांटम श्रेष्ठता का अर्थ यह है कि एक क्वांटम संगणक ने वह काम कर दिखाया जो किसी भी "अक्वांटम" संगणक की पहुंच के बाहर है। यदि हम ऐसे ही प्रवेग से आगे बढ़ते रहें तो कुछ सालों में रसायनविज्ञान और औषधीय अनुसंधान में अप्रतिम सिद्धियाँ हाँसिल करना शुरू कर देंगे। और क्या पता, आनेवाली पीढ़ियाँ शायद क्वांटम इंटरनेट की आदी बन जाएँ! </p>
      <p> यहाँ मैं आपको खुद आई.बी. एम. के क्वांटम संगणकों पर (<a href="https://www.ibm.com/quantum-computing/technology/experience/">IBM Quantum Experience</a> योजना के तहत) क्वांटम संगणन करने का अवसर प्रदान कर रहा हूँ- एक मज़ेदार तरीके से। आप सचमुच बैठे बैठे यहाँ असली क्वांटम संगणकों का इस्तेमाल करने वाले हैं!</p>
      <p> दिलचस्पी रखने वालों के लिए: पड़दे के पीछे <a href="https://qiskit.org/">IBM Qiskit  </a> प्रोग्रामिंग भाषा का उपयोग किया गया है। </p>
    <br>
    <br>
    <br>
  <h2> एक क्वांटम द्विचर के साथ खेल कूद (1 qubit) </h2>
    <p>क्यूबिट (क्वांटम द्विचर) परिचय, या आपकी निजी "स्च्रोडिंगेर बिल्ली": सबसे पहले आप एक क्वांटम द्विचर तैयार करें। सरल शब्दों में यह एक क्वांटम बिल्ली है - जो जिवंत (+) और मृत (-) दोनों अवस्था में रहती है। </p>
    <p> क्वांटम द्विचर तैयार होने पर आप इसे एक पासे की तरह उछाल सकते हैं - तकरीबन आधी बार जवाब "+" आएगा और बाकी के समय "-" ।  निम्न बटन दबाने पर क्वांटम संगणक 100 बार यह प्रयोग करेगा और आपको परिणाम दिखायेगा:</p>
    <br>
    <form method="post" action =".">
        <h4 class="text-center"><input type="submit" name="task1" value="एक क्वांटम द्विचर को बार बार नापें (measure 1 qubit multiple times)"></h4>
    </form>
    <strong><p  class="text-center"> बटन दबाने के बाद कृपया प्रतीक्षा करें। आई.बी.एम. का क्वांटम संगणक व्यस्त हो  सकता है ..... </p>
    </strong>
    <br>
    <br>
    <br>
    <h2> दो क्वांटम द्विचर के साथ खेल कूद- देउत्स्च कलन विधि (2 qubits) </h2> </u>
    <p> दोस्तों अभी तो हमने एक बेहद आसान क्वांटम संगणन कार्य किया। पर अभी कुछ पेचीदा करते हैं। दूसरे कार्य में आप ये समझेंगे कि क्वांटम संगणन क्यों शक्तिशाली है। </p>
    <p> मान लीजिये आपके पास एक प्रोग्राम है जो 0 या 1 इनपुट लेता है और 0 या 1 आउटपुट बतौर आउटपुट देता है। आपके पास दो विकल्प हैं - या तो यह प्रोग्राम "संतुलित" (balanced) है , वरना यह प्रोग्राम स्थिर (constant) है। संतुलित प्रोग्राम 0,1 देने पर दोनों बार अलग आउटपुट देता है। जब कि स्थिर प्रोग्राम 0, 1 देने पर या तो दोनों  बार 0 अथवा दोनों बार 1 देता है। </p>
    <img class="center-block" src="static/constbal.png" alt="function schematic" style="width:50%">
    <p> अब एक आम, अक्वांटम संगणक सिर्फ एक बार प्रोग्राम चलाकर यह नहीं कह सकता कि प्रोग्राम स्थिर (constant) है या फिर संतुलित (balanced) है। (ज़रा सोचिये इस बारे में) </p>
    <p> तो फिर क्वांटम संगणक क्या यह एक ही बार प्रोग्राम चलाकर हमें जवाब दे सकता है क्या? याद कीजिये क्वांटम पदार्थों के भिड़ाव के बारे में! यदि हम दो क्वांटम पदार्थों को निम्न स्थिति में ला सकते हैं, तो यह काम सरल हो सकता है। </p>
    <p> अधिक जानकारी के लिए <a href="https://arxiv.org/abs/1903.04359">यहाँ </a> जाएँ। </p>
    <img class="center-block" src="static/Deutsch.png" alt="Deutsch algorithm figure" style="width:70%">
    <h3 class="text-center"> यहाँ आपके लिए IBM का क्वांटम संगणक देउत्स्च कलन विधि (Deutsch algorithm) चलाएगा और अपना जवाब आपको बताएगा। </h3>

    <h4 class="text-center"> अपना फलन (function) चुनें (1-4 के बीच में, चार निम्नलिखित विकल्प): </h4>
    <h4 class="text-center"> 1: '(0,1) → (0,1)', 2: '(0,1) → (1,0)', 3: '(0,1) → (0,0)', 4: '(0,1) → (1,1)' </h4>
    <h4 class="text-center"> Enter your function choice: </h4>
    <form method="post" action =".">
        <p class="text-center"><input name="choice"></p>
        <br>
        <h4 class="text-center"><input type="submit" name="task2" value="देउत्स्च कलन विधि (Deutsch algorithm)" /></h4>
    <strong><p class="text-center"> बटन दबाने के बाद कृपया प्रतीक्षा करें। आई.बी.एम. का क्वांटम संगणक व्यस्त हो  सकता है ..... </p>
    </strong>
</form>
    </div>


    <div class="col-sm-2 sidenav">
      <h4 class="text-center"> Popular quantum computing blogs (नामचीन क्वांटम संगणन ब्लॉग) </h4>
      <div class="well">
            <a href="https://www.ibm.com/blogs/research/category/quantcomp/"> IBM (आई बी एम)</a>
        </div>
      <div class="well">
            <a href="https://www.scottaaronson.com/blog/"> Scott Aaronson (स्कॉट आरोनसन)
</a>
        </div>
      <div class="well">
            <a href="https://newsroom.intel.com/tag/quantum-computing/#gs.6h2v71"> Intel (इंटेल)</a>
        </div>
      <div class="well">
            <a href="https://www.sciencedaily.com/news/matter_energy/quantum_computing/"> Science Daily (साइंस डेली)</a>
        </div>
      <div class="well">
            <a href="https://gizmodo.com/tag/quantum-computers"> Gizmodo (गिज़मोडो)</a>
        </div>
      <div class="well">
            <a href="https://cloudblogs.microsoft.com/quantum/"> Microsoft (माइक्रोसॉफ्ट)</a>
        </div>
      <div class="well">
            <a href="https://blogs.wsj.com/cio/tag/quantum-computing/"> Wall Street Journal (वाल स्ट्रीट पत्रिका) </a>
        </div>
    </div>
  </div>
</div>

<footer class="container-fluid text-center">
  <p>Last update: May 2020. Contact prannerta100@gmail.com for issues.</p>
</footer>

</body>
</html>
    '''

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
