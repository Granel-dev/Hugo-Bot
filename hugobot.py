import streamlit as st
import random
# python -m  streamlit run c:/Users/arman/practiceStation/hugobot.py
st.markdown("""
       <style>
          .p{
            margin-top: 100px;
            font-size: 20px;  
          }
          .hugot{
            margin-top: 100px;
          }
       </style>
       <html>
         <center>
           <h1>Hugo-Bot</h1><br>
           <h2>Pusong Hirap Umamin E-Hugot Natin!!!</h2>
        
         </center>  
           <p class="p">Hit the enter button bellow to generate random hugot</p>
           <p>note the hugot line are not mine no plagiarism and no infringment intended this for entertainment only credits to all owners of hugot lines Reference https://pinoycollection.com</p>
       </html>
            """,unsafe_allow_html=True)
sad = ["Ikaw na nga yung nasaktan… Ikaw pa ang nag so-sorry.","Pinagtagpo kayo ng tadhana pero di kayo ang itinakda.","Bawal masaktan, lalo na kung crush pa lang.",
       "Si crush madaling titigan pero mahirap lapitan.","Darating yung panahon na titigan na lang kita sa paraang nakilala kita at hindi sa paraang minahal kita ng sobra.",
       "Sana tsinelas na lang tayong dalawa. Para kung mawala ang isa, di na pwedeng ipares sa iba kasi hindi na bagay.",]
joke = ["Papel. Minsan office supply. Madalas ikaw!","Para kang sunrise. PASIKAT.","Ang crush ay parang Math problem.Kung hindi mo makuha…Titigan mo na lang.",
        "My toes, may knees, my crush is manhid.","Iba ang crush sa mahal. Bakit ka nagseselos?","Pakainin kaya kita ng madaming kalabasa? Para makita mo namang nandito ako para sa’yo",
        "Alam mo ba yung salitang MANHID? Ikaw yun.","Kung camera lang ang mata, memory full na ‘to sa sobrang dami ng stolen shots mo.",
        "Huwag mong itanong kung ano ang gusto ko. Baka madulas lang ako at masabi kong ikaw ang gusto ko.","Ang hirap sa’yo… Sobrang manhid mo.",
        "Di bale ng di ako crush ng crush ko, di din naman siya crush ng crush niya!","Kung patay na patay ka sa isang taong nabubuhay para sa iba… Condolence, bes!",
        "Tumakbo ako para magpapayat. Hindi para habulin siya.","Buti pa ang loan, nagma-mature. Ikaw kaya?","Bakit ba ang tipid mong mag-reply? May pinag-iipunan ka ba?",
        "Sawa ka na ba sa buhay mo? Subukan mo naman sa buhay ko.","Sabi ni Peter Pan, “When you think happy thoughts, you’ll fly.” Pero bakit nung naisip kita, I fall?",
        "Sabi ni Peter Pan, “When you think happy thoughts, you’ll fly.” Pero bakit nung naisip kita, I fall?","Kasali ka daw sa GANG? Gang tingin na lang",
        "Lakas makaakyat ng bundok pero di makaakyat ng ligaw!","Pedicab ka ba? Pedicabang i-date sa Valentine’s Day?","Paglaki ko, gusto kong maging sa’yo! Happy heart’s day!",
        "Kasali nga pala ako sa FRAT. FRATing single. Happy Valentine’s to me!","Kung walang patutunguhan ang buhay mo, handa akong ituro sa’yo ang daan patungo sa puso ko.",
        "Sumalangit nawa ang puso kong patay na patay sa’yo. Maligayang araw ng mga puso!","Pinilit kong maging bakal ang puso ko. Hindi ko alam, gawa pala sa magnet ‘yang sa’yo. Happy heart’s day, beh!",
        "Relationship status: M.U. (Mag-isang umibig)","X’. Minsan letra. Madalas mahal mo pa."]
serious = ["Simpleng paghanga lang ang nararamdaman ko para sayo pero seryoso ako.","Mahalin mo ako kahit biro lang… Ako na’ng bahalang sumiryoso.","Fidget spinner ang paikutin mo, wag ako!",
           "Pag-sisid. Minsan parang pag-ibig. Kung kailan lumalalim, saka lumalamig.","Tadhana. Minsan kakampi mo. Minsan kalaro mo.","Ang pagmamahal ko sa’yo ay parang pagbebenta ng taho. Mabigat mang dalhin, ipagsisigawan ko pa rin.",
           "Naghintay ako. May hinihintay ka palang iba.",""]
st.write("please select hugot categories")
category = ["joke","sad","serious"]
if "select" not in st.session_state:
  st.session_state.select = " "
option = [sel for sel in category]
hugot = None
st.session_state.select = st.selectbox("category",option)
if st.session_state.select == "joke":
  hugot = joke
elif st.session_state.select == "sad":
  hugot = sad
elif st.session_state.select == "serious":
  hugot = serious
else:
  pass
hugot = random.choice(hugot)  
st.markdown(f"""
            <html>
            <div style='width:800px; height: 250px; border:1px solid gray; border-radius: 10px;'>
               <center><p class='hugot'>{hugot}</p></center>
            </div>
            </html>    
            """,unsafe_allow_html=True)
st.write("  ")
st.button("click")