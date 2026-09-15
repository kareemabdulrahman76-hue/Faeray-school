from pathlib import Path
import zipfile, textwrap

root = Path("/mnt/data/faeray-school")
(root / "css").mkdir(parents=True, exist_ok=True)
(root / "js").mkdir(parents=True, exist_ok=True)
(root / "assets").mkdir(parents=True, exist_ok=True)

html = r'''<!doctype html>
<html lang="en-NG">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0b3d2e">
  <meta name="description" content="Faeray School of Foundation — a Nigerian foundation school combining rigorous Western education with Islamic scholarship, character and leadership.">
  <title>Faeray School of Foundation | Knowledge, Faith & Excellence</title>
  <link rel="icon" type="image/svg+xml" href="assets/faeray-icon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>

  <header class="site-header" id="siteHeader">
    <div class="container nav-wrap">
      <a class="brand" href="#home" aria-label="Faeray School of Foundation home">
        <img src="assets/faeray-icon.svg" alt="" width="42" height="42">
        <span><strong>FAERAY</strong><small>School of Foundation</small></span>
      </a>

      <button class="menu-toggle" aria-expanded="false" aria-controls="primaryNav" aria-label="Open navigation">
        <span></span><span></span><span></span>
      </button>

      <nav id="primaryNav" class="primary-nav" aria-label="Primary navigation">
        <a href="#about">About</a>
        <a href="#programmes">Programmes</a>
        <a href="#advantage">Our Advantage</a>
        <a href="#life">School Life</a>
        <a href="#admissions">Admissions</a>
        <a class="nav-cta" href="#contact">Book a Visit</a>
      </nav>
    </div>
  </header>

  <main id="main">
    <section class="hero" id="home">
      <div class="hero-pattern" aria-hidden="true"></div>
      <div class="container hero-grid">
        <div class="hero-copy reveal">
          <div class="eyebrow"><span></span> 2026/2027 Admissions Now Open</div>
          <h1>Where <em>faith</em> meets a future of excellence.</h1>
          <p class="hero-lead">Faeray School of Foundation develops confident Nigerian learners through a purposeful blend of Islamic scholarship, rigorous Western academics, character formation and modern skills.</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="#admissions">Start an Application <span>↗</span></a>
            <a class="btn btn-ghost" href="#about">Discover Faeray</a>
          </div>
          <div class="trust-row" aria-label="School highlights">
            <div><strong>01</strong><span>Faith & Character</span></div>
            <div><strong>02</strong><span>Academic Rigour</span></div>
            <div><strong>03</strong><span>Future Readiness</span></div>
          </div>
        </div>

        <div class="hero-card reveal" aria-label="Faeray learning philosophy">
          <div class="arch"></div>
          <div class="hero-card-content">
            <span class="card-kicker">THE FAERAY PROMISE</span>
            <div class="arabic-mark" aria-hidden="true">اقرأ</div>
            <h2>Learn deeply.<br>Live honourably.<br>Lead confidently.</h2>
            <p>Knowledge is the foundation. Character is the compass. Excellence is the standard.</p>
            <div class="seal-row"><span>Est. 2012</span><i></i><span>Lagos, Nigeria</span></div>
          </div>
        </div>
      </div>
      <div class="scroll-cue" aria-hidden="true">Scroll to explore <span>↓</span></div>
    </section>

    <section class="intro section" id="about">
      <div class="container two-col">
        <div class="section-heading reveal">
          <span class="section-label">01 / WHO WE ARE</span>
          <h2>A strong beginning for an exceptional future.</h2>
        </div>
        <div class="intro-copy reveal">
          <p class="lead">Faeray is a Nigerian school of foundation built for families who want their children to grow intellectually, spiritually and socially — without having to choose between them.</p>
          <p>Our learning model brings the Nigerian curriculum into conversation with Islamic studies, Arabic, Qur'anic learning, digital literacy, communication, leadership and creative discovery. The result is an education that prepares pupils for examinations while preparing them for life.</p>
          <a class="text-link" href="#programmes">Explore our programmes <span>→</span></a>
        </div>
      </div>
    </section>

    <section class="stats-band">
      <div class="container stats-grid">
        <div><strong>14<span>+</span></strong><p>Years shaping young minds</p></div>
        <div><strong>1:12</strong><p>Target learner-to-teacher ratio</p></div>
        <div><strong>3</strong><p>Dimensions: Faith · Academics · Life</p></div>
        <div><strong>21<span>st</span></strong><p>Century skills embedded in learning</p></div>
      </div>
    </section>

    <section class="programmes section" id="programmes">
      <div class="container">
        <div class="section-top reveal">
          <div>
            <span class="section-label">02 / ACADEMICS</span>
            <h2>Two traditions.<br><em>One complete education.</em></h2>
          </div>
          <p>Our programmes are designed to complement one another — building strong academic foundations while cultivating adab, curiosity, discipline and leadership.</p>
        </div>

        <div class="programme-grid">
          <article class="programme-card light reveal">
            <div class="number">01</div>
            <div class="programme-icon">⌁</div>
            <h3>Western Academics</h3>
            <p>Structured learning across literacy, mathematics, sciences, humanities, technology and the arts, aligned with the Nigerian basic education framework.</p>
            <ul>
              <li>Core Nigerian curriculum</li>
              <li>Literacy, numeracy & science</li>
              <li>ICT, coding & digital citizenship</li>
              <li>Project-based learning</li>
            </ul>
          </article>

          <article class="programme-card dark reveal">
            <div class="number">02</div>
            <div class="programme-icon">۞</div>
            <h3>Islamic Scholarship</h3>
            <p>A thoughtful Islamic programme centred on Qur'an, Arabic, Islamic studies, adab and values that guide students in school, family and society.</p>
            <ul>
              <li>Qur'anic recitation & memorisation</li>
              <li>Arabic language foundations</li>
              <li>Islamic studies & seerah</li>
              <li>Adab, ethics & service</li>
            </ul>
          </article>

          <article class="programme-card accent reveal">
            <div class="number">03</div>
            <div class="programme-icon">✦</div>
            <h3>Future Skills</h3>
            <p>Beyond the textbook: students practise communication, problem-solving, creativity, collaboration and responsible technology use.</p>
            <ul>
              <li>Public speaking & debate</li>
              <li>Entrepreneurial thinking</li>
              <li>STEM, robotics & innovation</li>
              <li>Leadership & community service</li>
            </ul>
          </article>
        </div>
      </div>
    </section>

    <section class="advantage section" id="advantage">
      <div class="container advantage-grid">
        <div class="advantage-visual reveal">
          <div class="visual-panel">
            <span class="vertical-label">THE FAERAY ADVANTAGE</span>
            <div class="quote-mark">“</div>
            <blockquote>We do not simply prepare children to pass. We prepare them to become.</blockquote>
            <div class="quote-line"></div>
            <p>— The Faeray Learning Philosophy</p>
          </div>
        </div>
        <div class="advantage-copy">
          <span class="section-label">03 / WHY FAERAY</span>
          <h2>An environment designed to bring out <em>excellence.</em></h2>
          <div class="feature-list">
            <article class="feature reveal"><span>01</span><div><h3>Formation, not just instruction</h3><p>Daily routines, mentorship and purposeful activities turn values such as honesty, discipline, responsibility and service into lived habits.</p></div></article>
            <article class="feature reveal"><span>02</span><div><h3>Individual attention</h3><p>Small learning groups and regular formative assessment help teachers identify strengths, close gaps and challenge learners appropriately.</p></div></article>
            <article class="feature reveal"><span>03</span><div><h3>Rooted in Nigeria, ready for the world</h3><p>Students develop a strong sense of identity alongside the communication, digital and critical-thinking skills needed in a connected world.</p></div></article>
            <article class="feature reveal"><span>04</span><div><h3>Partnership with parents</h3><p>Clear communication and structured progress updates help families participate meaningfully in each child's educational journey.</p></div></article>
          </div>
        </div>
      </div>
    </section>

    <section class="life section" id="life">
      <div class="container">
        <div class="section-top reveal">
          <div><span class="section-label">04 / SCHOOL LIFE</span><h2>Learning continues<br><em>beyond the classroom.</em></h2></div>
          <p>Students discover talents, build friendships and practise leadership through a balanced programme of clubs, sport, creativity and service.</p>
        </div>
        <div class="life-grid">
          <div class="life-card large reveal"><span>STEM & INNOVATION</span><h3>Build. Test.<br>Improve.</h3><p>Hands-on challenges in coding, science and design turn curiosity into practical problem-solving.</p></div>
          <div class="life-card reveal"><span>LANGUAGES</span><h3>English · Arabic<br>Hausa · Yoruba</h3><p>Language builds confidence, culture and connection.</p></div>
          <div class="life-card reveal"><span>LEADERSHIP</span><h3>Find your<br>voice.</h3><p>Debate, public speaking, student leadership and service projects.</p></div>
          <div class="life-card wide reveal"><span>SPORT & WELLNESS</span><h3>Move well. Play fair. Grow together.</h3><p>Football, athletics, indoor games and wellness activities encourage teamwork, resilience and healthy routines.</p></div>
        </div>
      </div>
    </section>

    <section class="admissions section" id="admissions">
      <div class="container admissions-grid">
        <div class="admissions-copy reveal">
          <span class="section-label">05 / ADMISSIONS</span>
          <h2>Give your child a <em>foundation</em> worth building on.</h2>
          <p>Admissions for the 2026/2027 academic session are open for qualified applicants. Our process is designed to help families understand Faeray and help us understand each learner.</p>
          <div class="steps">
            <div><span>01</span><p><strong>Register interest</strong><small>Complete the enquiry form.</small></p></div>
            <div><span>02</span><p><strong>Assessment</strong><small>Age-appropriate academic and readiness assessment.</small></p></div>
            <div><span>03</span><p><strong>Family conversation</strong><small>Meet our admissions team and tour the school.</small></p></div>
            <div><span>04</span><p><strong>Offer & enrolment</strong><small>Receive placement details and complete registration.</small></p></div>
          </div>
        </div>

        <form class="admission-form reveal" id="admissionForm" novalidate>
          <div class="form-head"><span>ADMISSIONS ENQUIRY</span><h3>Start here.</h3><p>Tell us a little about your family and we'll get in touch.</p></div>
          <label>Parent / Guardian name<input name="name" required autocomplete="name" placeholder="e.g. Amina Yusuf"><span class="error"></span></label>
          <label>Email address<input name="email" type="email" required autocomplete="email" placeholder="you@example.com"><span class="error"></span></label>
          <label>Phone number<input name="phone" type="tel" required autocomplete="tel" placeholder="+234 800 000 0000"><span class="error"></span></label>
          <label>Year group<select name="year" required><option value="">Select year group</option><option>Early Years</option><option>Primary</option><option>Junior Secondary (JSS)</option><option>Senior Secondary (SSS)</option></select><span class="error"></span></label>
          <button class="btn btn-primary full" type="submit">Submit Enquiry <span>→</span></button>
          <p class="form-note">Demo form for this website concept. Connect it to your preferred backend or form service before launch.</p>
        </form>
      </div>
    </section>

    <section class="faq section">
      <div class="container faq-grid">
        <div class="section-heading reveal"><span class="section-label">06 / QUESTIONS</span><h2>Frequently asked.</h2><p>Everything you need to know before taking the next step.</p></div>
        <div class="accordion reveal">
          <button class="faq-item" aria-expanded="false"><span>What makes Faeray's education different?</span><b>+</b></button>
          <div class="faq-answer"><p>Faeray intentionally integrates rigorous Nigerian academic learning with Islamic scholarship, character development and future-focused skills, giving learners a coherent education rather than separate tracks.</p></div>
          <button class="faq-item" aria-expanded="false"><span>Which examination pathways do you prepare learners for?</span><b>+</b></button>
          <div class="faq-answer"><p>For the relevant secondary years, the school prepares learners for Nigerian examination pathways such as WAEC and NECO, while building the broader skills needed for tertiary education.</p></div>
          <button class="faq-item" aria-expanded="false"><span>Is Islamic education compulsory?</span><b>+</b></button>
          <div class="faq-answer"><p>Faeray is presented as a faith-based school where Islamic learning and character formation are integral to the educational experience. Specific programme requirements should be confirmed with the admissions office.</p></div>
          <button class="faq-item" aria-expanded="false"><span>Can parents visit before applying?</span><b>+</b></button>
          <div class="faq-answer"><p>Yes. Families can request a campus visit and admissions conversation so they can experience the learning environment and discuss the appropriate entry point for their child.</p></div>
        </div>
      </div>
    </section>

    <section class="final-cta" id="contact">
      <div class="container final-inner reveal">
        <span class="section-label">BEGIN THE JOURNEY</span>
        <h2>Build a foundation<br><em>that lasts a lifetime.</em></h2>
        <p>Faeray School of Foundation · Lagos, Nigeria</p>
        <div class="cta-actions"><a class="btn btn-light" href="#admissions">Apply for 2026/2027 <span>↗</span></a><a class="contact-link" href="mailto:admissions@faerayschool.ng">admissions@faerayschool.ng</a></div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container footer-grid">
      <div class="footer-brand"><a class="brand" href="#home"><img src="assets/faeray-icon.svg" alt="" width="42" height="42"><span><strong>FAERAY</strong><small>School of Foundation</small></span></a><p>Knowledge. Faith. Excellence.</p></div>
      <div><h4>Explore</h4><a href="#about">About</a><a href="#programmes">Academics</a><a href="#advantage">Our Advantage</a><a href="#life">School Life</a></div>
      <div><h4>Admissions</h4><a href="#admissions">Apply</a><a href="#admissions">Book a Visit</a><a href="#faq">FAQs</a></div>
      <div><h4>Contact</h4><p>14 Crescent Avenue,<br>GRA Ikeja, Lagos, Nigeria</p><a href="tel:+2348090002026">+234 809 000 2026</a><a href="mailto:hello@faerayschool.ng">hello@faerayschool.ng</a></div>
    </div>
    <div class="container footer-bottom"><span>© 2026 Faeray School of Foundation. Concept website.</span><span>Designed for a Nigerian learning community.</span></div>
  </footer>

  <div class="toast" id="toast" role="status" aria-live="polite">Thank you — your enquiry has been received.</div>
  <script src="js/main.js"></script>
</body>
</html>'''

css = r''':root{
  --green:#0b3d2e;--green-2:#124f3c;--cream:#f6f0e5;--paper:#fbfaf7;--gold:#c79a4a;--gold-soft:#ead8ad;
  --ink:#16231e;--muted:#66736d;--line:#dfe3dc;--white:#fff;--radius:22px;--shadow:0 20px 60px rgba(16,43,34,.12);
  --display:"Playfair Display",Georgia,serif;--body:"DM Sans",Arial,sans-serif;
}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--body);line-height:1.65;overflow-x:hidden}
a{color:inherit;text-decoration:none}button,input,select{font:inherit}.container{width:min(1160px,calc(100% - 40px));margin:auto}
.skip-link{position:fixed;left:16px;top:-60px;background:#fff;padding:10px 14px;z-index:1000}.skip-link:focus{top:16px}
.site-header{position:fixed;inset:0 0 auto;z-index:50;transition:.3s;background:rgba(251,250,247,.76);backdrop-filter:blur(14px);border-bottom:1px solid transparent}.site-header.scrolled{box-shadow:0 8px 30px rgba(15,40,31,.08);border-color:var(--line)}
.nav-wrap{height:82px;display:flex;align-items:center;justify-content:space-between}.brand{display:flex;align-items:center;gap:10px}.brand img{width:42px;height:42px}.brand strong{display:block;font-size:15px;letter-spacing:.17em;line-height:1}.brand small{display:block;font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-top:6px}
.primary-nav{display:flex;align-items:center;gap:26px;font-size:13px;font-weight:600}.primary-nav a:not(.nav-cta){position:relative}.primary-nav a:not(.nav-cta):after{content:"";position:absolute;left:0;bottom:-8px;width:0;height:1px;background:var(--green);transition:.25s}.primary-nav a:not(.nav-cta):hover:after{width:100%}.nav-cta{background:var(--green);color:#fff;padding:11px 17px;border-radius:99px}
.menu-toggle{display:none;background:none;border:0;width:44px;height:44px}.menu-toggle span{display:block;height:2px;background:var(--green);margin:6px 8px}
.hero{min-height:780px;background:var(--cream);position:relative;padding:150px 0 80px;display:flex;align-items:center;overflow:hidden}.hero-pattern{position:absolute;width:700px;height:700px;border:1px solid rgba(11,61,46,.1);border-radius:50%;right:-240px;top:-160px}.hero-pattern:before,.hero-pattern:after{content:"";position:absolute;border:1px solid rgba(11,61,46,.07);border-radius:50%;inset:70px}.hero-pattern:after{inset:140px}.hero-grid{display:grid;grid-template-columns:1.05fr .8fr;gap:90px;align-items:center;position:relative}.eyebrow,.section-label,.card-kicker{font-size:11px;letter-spacing:.17em;font-weight:800;color:var(--green);text-transform:uppercase}.eyebrow{display:flex;gap:9px;align-items:center;margin-bottom:22px}.eyebrow span{width:30px;height:1px;background:var(--gold)}
h1,h2,h3{font-family:var(--display);line-height:1.08;margin:0}h1{font-size:clamp(50px,6vw,82px);letter-spacing:-.045em;max-width:760px}h1 em,h2 em{color:var(--gold);font-style:normal}.hero-lead{max-width:650px;font-size:17px;color:#52615a;margin:25px 0 32px}.hero-actions{display:flex;gap:12px;flex-wrap:wrap}.btn{display:inline-flex;justify-content:center;align-items:center;gap:18px;border:0;border-radius:999px;padding:15px 21px;font-weight:700;cursor:pointer;transition:transform .2s,box-shadow .2s,background .2s}.btn:hover{transform:translateY(-2px)}.btn-primary{background:var(--green);color:#fff;box-shadow:0 10px 24px rgba(11,61,46,.18)}.btn-primary:hover{background:#092f24}.btn-ghost{border:1px solid #bdc7c0;background:transparent}.btn-light{background:#fff;color:var(--green)}.trust-row{display:flex;gap:30px;margin-top:55px;padding-top:23px;border-top:1px solid #d8d6ca}.trust-row div{display:flex;gap:9px;align-items:center}.trust-row strong{font-family:var(--display);color:var(--gold);font-size:20px}.trust-row span{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.08em}
.hero-card{background:var(--green);color:#fff;border-radius:180px 180px 24px 24px;min-height:510px;position:relative;box-shadow:var(--shadow);overflow:hidden}.arch{position:absolute;inset:18px;border:1px solid rgba(255,255,255,.18);border-radius:165px 165px 18px 18px}.hero-card-content{position:absolute;inset:0;padding:90px 55px 45px;display:flex;flex-direction:column;align-items:center;text-align:center}.card-kicker{color:var(--gold-soft)}.arabic-mark{font-size:58px;font-family:Georgia,serif;margin:25px 0 18px;color:#ead8ad}.hero-card h2{font-size:32px}.hero-card p{font-size:13px;color:#cbd9d3;max-width:290px;margin-top:22px}.seal-row{margin-top:auto;display:flex;gap:15px;align-items:center;font-size:10px;letter-spacing:.13em;text-transform:uppercase;color:#b9c9c2}.seal-row i{width:4px;height:4px;background:var(--gold);border-radius:50%}.scroll-cue{position:absolute;bottom:25px;left:50%;transform:translateX(-50%);font-size:10px;text-transform:uppercase;letter-spacing:.16em;color:#718079;display:flex;gap:12px}.scroll-cue span{font-size:16px}
.section{padding:125px 0}.two-col{display:grid;grid-template-columns:.8fr 1.2fr;gap:100px}.section-heading h2,.section-top h2,.advantage-copy>h2,.admissions-copy h2{font-size:clamp(38px,4.3vw,60px);letter-spacing:-.04em;margin-top:17px}.intro-copy .lead{font-size:22px;line-height:1.5;color:#263a32;margin-top:0}.intro-copy p:not(.lead){color:var(--muted);max-width:680px}.text-link{display:inline-flex;gap:14px;margin-top:18px;font-weight:800;color:var(--green);border-bottom:1px solid var(--gold);padding-bottom:5px}.text-link span{transition:.2s}.text-link:hover span{transform:translateX(5px)}
.stats-band{background:var(--green);color:#fff;padding:43px 0}.stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}.stats-grid>div{padding-left:24px;border-left:1px solid rgba(255,255,255,.18)}.stats-grid strong{font-family:var(--display);font-size:42px;line-height:1}.stats-grid strong span{font-size:20px;color:var(--gold)}.stats-grid p{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:#c2d1ca;margin:8px 0 0}
.programmes{background:#f0ece3}.section-top{display:flex;justify-content:space-between;align-items:end;gap:60px;margin-bottom:55px}.section-top>p{max-width:410px;color:var(--muted);margin:0}.programme-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.programme-card{border-radius:var(--radius);padding:36px;min-height:430px;position:relative;overflow:hidden}.programme-card.light{background:#fff}.programme-card.dark{background:var(--green);color:#fff}.programme-card.accent{background:#d5b36b;color:#19251f}.programme-card .number{font-size:11px;letter-spacing:.15em;font-weight:800;opacity:.6}.programme-icon{font-size:34px;margin:34px 0 20px;color:var(--gold)}.programme-card h3{font-size:28px}.programme-card p{font-size:14px;opacity:.75}.programme-card ul{list-style:none;padding:0;margin:26px 0 0;font-size:12px;font-weight:700}.programme-card li{padding:8px 0;border-top:1px solid currentColor;opacity:.7}
.advantage{background:#fff}.advantage-grid{display:grid;grid-template-columns:.85fr 1.15fr;gap:100px;align-items:center}.visual-panel{height:620px;background:var(--green);color:#fff;border-radius:220px 220px 24px 24px;position:relative;padding:110px 70px 60px;overflow:hidden}.visual-panel:after{content:"";position:absolute;width:500px;height:500px;border:1px solid rgba(255,255,255,.11);border-radius:50%;top:70px;left:50%;transform:translateX(-50%)}.vertical-label{position:absolute;left:28px;top:50%;writing-mode:vertical-rl;transform:rotate(180deg);font-size:9px;letter-spacing:.2em;color:#9bb2a7}.quote-mark{font-family:Georgia;font-size:100px;color:var(--gold);line-height:.7;position:relative;z-index:1}.visual-panel blockquote{font-family:var(--display);font-size:34px;line-height:1.2;position:relative;z-index:1;margin:25px 0}.quote-line{height:1px;background:rgba(255,255,255,.25);position:relative;z-index:1}.visual-panel>p{font-size:11px;color:#a9bbb3;position:relative;z-index:1}.feature-list{margin-top:35px}.feature{display:grid;grid-template-columns:45px 1fr;gap:20px;padding:23px 0;border-top:1px solid var(--line)}.feature>span{font-family:var(--display);font-size:18px;color:var(--gold)}.feature h3{font-family:var(--body);font-size:16px;font-weight:800}.feature p{font-size:13px;color:var(--muted);margin:7px 0 0}
.life{background:var(--cream)}.life-grid{display:grid;grid-template-columns:1.3fr .7fr;grid-auto-rows:250px;gap:16px}.life-card{padding:35px;border-radius:var(--radius);background:#fff;position:relative;overflow:hidden;display:flex;flex-direction:column;justify-content:end}.life-card.large{grid-row:span 2;background:var(--green);color:#fff}.life-card.wide{background:#d5b36b;grid-column:span 2}.life-card:before{content:"";position:absolute;width:190px;height:190px;border:1px solid rgba(11,61,46,.1);border-radius:50%;right:-50px;top:-50px}.life-card span{font-size:9px;letter-spacing:.18em;font-weight:800;color:var(--gold);position:relative}.life-card h3{font-size:30px;position:relative;margin:12px 0}.life-card p{font-size:13px;max-width:380px;opacity:.72;position:relative;margin:0}.life-card.large h3{font-size:48px}.life-card.large:before{border-color:rgba(255,255,255,.1);width:300px;height:300px}
.admissions{background:var(--green);color:#fff}.admissions-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:100px;align-items:start}.admissions-copy>p{color:#b9cbc3;max-width:600px;margin:25px 0}.steps{margin-top:42px}.steps>div{display:grid;grid-template-columns:40px 1fr;gap:18px;padding:17px 0;border-top:1px solid rgba(255,255,255,.16)}.steps span{font-family:var(--display);color:var(--gold);font-size:17px}.steps p{margin:0}.steps strong{display:block;font-size:14px}.steps small{display:block;color:#a9bbb3;margin-top:3px}.admission-form{background:#fff;color:var(--ink);border-radius:var(--radius);padding:34px;box-shadow:var(--shadow)}.form-head span{font-size:9px;letter-spacing:.18em;color:var(--gold);font-weight:800}.form-head h3{font-size:34px;margin-top:9px}.form-head p{font-size:12px;color:var(--muted)}label{display:block;font-size:11px;font-weight:800;margin-top:17px}input,select{width:100%;border:0;border-bottom:1px solid #cfd7d1;padding:11px 0;background:transparent;outline:none;border-radius:0;color:var(--ink);font-size:14px}input:focus,select:focus{border-color:var(--green);box-shadow:0 2px 0 var(--green)}.error{display:block;color:#a94442;font-size:10px;height:15px}.full{width:100%;margin-top:12px}.form-note{font-size:9px;color:#7a8580;text-align:center;margin:15px 0 0}
.faq{background:#fff}.faq-grid{display:grid;grid-template-columns:.7fr 1.3fr;gap:110px}.section-heading p{color:var(--muted)}.accordion{border-top:1px solid var(--line)}.faq-item{width:100%;background:none;border:0;border-bottom:1px solid var(--line);padding:22px 0;text-align:left;display:flex;justify-content:space-between;cursor:pointer;font-weight:800;color:var(--ink)}.faq-item b{font-size:22px;font-weight:400;color:var(--gold);transition:.2s}.faq-item[aria-expanded=true] b{transform:rotate(45deg)}.faq-answer{display:grid;grid-template-rows:0fr;transition:.3s}.faq-answer p{overflow:hidden;margin:0;color:var(--muted);font-size:13px}.faq-item[aria-expanded=true]+.faq-answer{grid-template-rows:1fr}.faq-item[aria-expanded=true]+.faq-answer p{padding:0 35px 22px 0}
.final-cta{background:var(--cream);padding:110px 0}.final-inner{text-align:center}.final-inner h2{font-size:clamp(48px,6vw,78px);letter-spacing:-.05em;margin:16px auto}.final-inner>p{color:var(--muted)}.cta-actions{display:flex;justify-content:center;align-items:center;gap:25px;flex-wrap:wrap;margin-top:30px}.contact-link{font-size:12px;font-weight:800;border-bottom:1px solid var(--gold);padding-bottom:4px}
.footer{background:#082d22;color:#dce7e1;padding:70px 0 20px}.footer-grid{display:grid;grid-template-columns:1.4fr .7fr .7fr 1fr;gap:60px}.footer .brand strong{color:#fff}.footer .brand small{color:#9eb2a8}.footer-brand>p{font-family:var(--display);color:#fff;margin-top:20px}.footer h4{font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);margin:0 0 18px}.footer-grid>div:not(.footer-brand) a,.footer-grid>div:not(.footer-brand) p{display:block;color:#aebfb7;font-size:12px;margin:7px 0}.footer-grid a:hover{color:#fff}.footer-bottom{border-top:1px solid rgba(255,255,255,.12);margin-top:50px;padding-top:18px;display:flex;justify-content:space-between;gap:20px;color:#718a80;font-size:10px}
.toast{position:fixed;right:20px;bottom:20px;background:var(--green);color:#fff;padding:14px 18px;border-radius:12px;box-shadow:var(--shadow);transform:translateY(130px);opacity:0;transition:.3s;z-index:100;font-size:12px}.toast.show{transform:none;opacity:1}.reveal{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease}.reveal.visible{opacity:1;transform:none}
@media(max-width:900px){.primary-nav{position:absolute;left:20px;right:20px;top:76px;background:#fff;padding:20px;border-radius:18px;box-shadow:var(--shadow);display:none;flex-direction:column;align-items:stretch}.primary-nav.open{display:flex}.nav-cta{text-align:center}.menu-toggle{display:block}.hero{min-height:auto;padding:135px 0 70px}.hero-grid,.two-col,.advantage-grid,.admissions-grid,.faq-grid{grid-template-columns:1fr;gap:55px}.hero-card{max-width:500px;width:100%;margin:auto}.section-top{align-items:start;flex-direction:column}.programme-grid{grid-template-columns:1fr}.stats-grid{grid-template-columns:repeat(2,1fr);gap:28px}.life-grid{grid-template-columns:1fr;grid-auto-rows:auto}.life-card,.life-card.large,.life-card.wide{grid-row:auto;grid-column:auto;min-height:250px}.footer-grid{grid-template-columns:1fr 1fr}}
@media(max-width:560px){.container{width:min(100% - 28px,1160px)}.nav-wrap{height:72px}.hero{padding-top:120px}.hero-card{min-height:470px}.hero-card-content{padding:82px 30px 35px}.trust-row{gap:14px;justify-content:space-between}.trust-row div{display:block}.trust-row span{display:block;margin-top:3px;font-size:8px}.section{padding:85px 0}.stats-grid{grid-template-columns:1fr 1fr}.stats-grid strong{font-size:32px}.visual-panel{height:500px;border-radius:150px 150px 20px 20px;padding:95px 45px 40px}.visual-panel blockquote{font-size:27px}.footer-grid{grid-template-columns:1fr 1fr;gap:35px}.footer-brand{grid-column:span 2}.footer-bottom{flex-direction:column}.admission-form{padding:25px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.reveal{opacity:1;transform:none;transition:none}.btn,.faq-item b{transition:none}}
'''

js = r'''const header = document.getElementById('siteHeader');
const menu = document.querySelector('.menu-toggle');
const nav = document.getElementById('primaryNav');

window.addEventListener('scroll', () => {
  header.classList.toggle('scrolled', window.scrollY > 20);
}, {passive:true});

menu.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  menu.setAttribute('aria-expanded', String(open));
  menu.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
});
nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  nav.classList.remove('open');
  menu.setAttribute('aria-expanded','false');
  menu.setAttribute('aria-label','Open navigation');
}));

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if(entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, {threshold:.12});
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

document.querySelectorAll('.faq-item').forEach(button => {
  button.addEventListener('click', () => {
    const expanded = button.getAttribute('aria-expanded') === 'true';
    document.querySelectorAll('.faq-item').forEach(item => item.setAttribute('aria-expanded','false'));
    button.setAttribute('aria-expanded', String(!expanded));
  });
});

const form = document.getElementById('admissionForm');
const toast = document.getElementById('toast');
form.addEventListener('submit', event => {
  event.preventDefault();
  let valid = true;
  form.querySelectorAll('[required]').forEach(field => {
    const error = field.parentElement.querySelector('.error');
    let message = '';
    if(!field.value.trim()) message = 'This field is required.';
    else if(field.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(field.value)) message = 'Enter a valid email address.';
    error.textContent = message;
    if(message) valid = false;
  });
  if(!valid) return;
  toast.classList.add('show');
  form.reset();
  setTimeout(() => toast.classList.remove('show'), 4500);
});
'''

svg = r'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96">
  <rect width="96" height="96" rx="24" fill="#0b3d2e"/>
  <path d="M48 12c12 12 28 15 36 16v24c0 18-13 27-36 34C25 79 12 70 12 52V28c8-1 24-4 36-16Z" fill="none" stroke="#c79a4a" stroke-width="3"/>
  <path d="M28 55c6-11 12-17 20-23 8 6 14 12 20 23-7-3-13-4-20-4s-13 1-20 4Z" fill="#ead8ad"/>
  <path d="M48 32v19M38 45h20" stroke="#0b3d2e" stroke-width="3" stroke-linecap="round"/>
  <circle cx="48" cy="62" r="3" fill="#c79a4a"/>
</svg>'''

(root/"index.html").write_text(html, encoding="utf-8")
(root/"css/style.css").write_text(css, encoding="utf-8")
(root/"js/main.js").write_text(js, encoding="utf-8")
(root/"assets/faeray-icon.svg").write_text(svg, encoding="utf-8")

zip_path = Path("/mnt/data/faeray-school-website.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for p in root.rglob("*"):
        if p.is_file():
            z.write(p, p.relative_to(root))

print(f"Created: {zip_path}")
print("Files:", [str(p.relative_to(root)) for p in root.rglob("*") if p.is_file()])
