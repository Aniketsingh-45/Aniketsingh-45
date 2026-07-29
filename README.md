<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mission Control — Aniket Singh</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
<style>
  :root{
    --void:#0A0E1A;
    --nebula:#141A2E;
    --nebula-2:#1C2340;
    --ion:#7C5CFF;
    --ion-soft:rgba(124,92,255,.16);
    --plasma:#2BD9C9;
    --plasma-soft:rgba(43,217,201,.16);
    --solar:#FFB454;
    --solar-soft:rgba(255,180,84,.16);
    --starlight:#F5F7FF;
    --mist:#AEB4CC;
    --line: rgba(255,255,255,.09);
    --shadow: 0 20px 60px -20px rgba(0,0,0,.6);
    --radius-lg: 22px;
    --radius-md: 14px;
    --radius-sm: 999px;
    --space-1:4px;--space-2:8px;--space-3:12px;--space-4:16px;--space-5:24px;--space-6:32px;--space-7:48px;--space-8:64px;
  }
  [data-theme="light"]{
    --void:#F3F5FB;
    --nebula:#FFFFFF;
    --nebula-2:#EEF0FA;
    --ion:#6A42FF;
    --ion-soft:rgba(106,66,255,.10);
    --plasma:#0E9C90;
    --plasma-soft:rgba(14,156,144,.10);
    --solar:#C97A12;
    --solar-soft:rgba(201,122,18,.12);
    --starlight:#141A2E;
    --mist:#565D7A;
    --line: rgba(10,14,26,.08);
    --shadow: 0 20px 50px -25px rgba(20,26,46,.25);
  }

  *{box-sizing:border-box;}
  html,body{margin:0;padding:0;}
  body{
    background:
      radial-gradient(circle at 15% -10%, var(--ion-soft), transparent 45%),
      radial-gradient(circle at 90% 0%, var(--plasma-soft), transparent 40%),
      var(--void);
    color:var(--starlight);
    font-family:'Inter',sans-serif;
    transition:background-color .4s ease, color .4s ease;
    padding:40px 20px 80px;
    min-height:100vh;
  }
  .mono{ font-family:'IBM Plex Mono',monospace; letter-spacing:.02em; }
  .display{ font-family:'Space Grotesk',sans-serif; }

  .wrap{ max-width:920px; margin:0 auto; }

  /* ===== HEADER ===== */
  .console{
    position:relative;
    background:linear-gradient(180deg, var(--nebula), var(--nebula-2));
    border:1px solid var(--line);
    border-radius:var(--radius-lg);
    box-shadow:var(--shadow);
    padding:var(--space-6) var(--space-6) var(--space-5);
    overflow:hidden;
  }
  .console::before{
    content:"";
    position:absolute; inset:0;
    background:
      linear-gradient(90deg, transparent 0%, var(--ion) 50%, transparent 100%);
    height:2px; top:0; left:0; right:0;
    opacity:.55;
  }
  .topbar{
    display:flex; justify-content:space-between; align-items:center;
    margin-bottom:var(--space-6);
  }
  .status{
    display:flex; align-items:center; gap:8px;
    font-size:11px; text-transform:uppercase; color:var(--mist);
  }
  .status .dot{
    width:7px;height:7px;border-radius:50%;background:var(--plasma);
    box-shadow:0 0 0 0 var(--plasma-soft);
    animation:pulseDot 2s infinite;
  }
  @keyframes pulseDot{
    0%{ box-shadow:0 0 0 0 var(--plasma-soft);}
    70%{ box-shadow:0 0 0 8px rgba(0,0,0,0);}
    100%{ box-shadow:0 0 0 0 rgba(0,0,0,0);}
  }

  /* theme toggle */
  .toggle{
    display:flex; align-items:center; gap:8px;
    background:var(--void); border:1px solid var(--line);
    border-radius:var(--radius-sm); padding:4px; cursor:pointer;
    font-size:12px;
  }
  .toggle button{
    all:unset; cursor:pointer; padding:6px 10px; border-radius:var(--radius-sm);
    color:var(--mist); font-size:14px; line-height:1; display:flex; align-items:center;
  }
  .toggle button.active{
    background:var(--ion-soft); color:var(--ion);
  }
  .toggle button:focus-visible{ outline:2px solid var(--ion); outline-offset:2px; }

  .hero{
    display:flex; align-items:center; gap:var(--space-6); flex-wrap:wrap;
  }

  .orbit-wrap{
    position:relative; width:104px; height:104px; flex:none;
  }
  .orbit-ring{
    position:absolute; inset:-14px;
    border-radius:50%;
    border:1.5px dashed var(--ion);
    opacity:.45;
    animation:spin 22s linear infinite;
  }
  .orbit-ring.r2{ inset:-26px; border-color:var(--plasma); opacity:.3; animation-duration:32s; animation-direction:reverse;}
  @keyframes spin{ to{ transform:rotate(360deg);} }
  .orbit-node{
    position:absolute; width:8px; height:8px; border-radius:50%;
    background:var(--solar); box-shadow:0 0 10px 2px var(--solar-soft);
    top:-4px; left:50%;
  }
  .avatar{
    width:104px; height:104px; border-radius:50%;
    background:linear-gradient(135deg, var(--ion), var(--plasma));
    display:flex; align-items:center; justify-content:center;
    font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:34px;
    color:#0A0E1A;
    position:relative; z-index:2;
  }

  .heading h1{
    font-size:32px; margin:0 0 6px; font-weight:700; letter-spacing:-.01em;
  }
  .heading .role{
    margin:0 0 14px; color:var(--mist); font-size:14px;
  }
  .typeline{
    font-size:13.5px; color:var(--plasma);
    display:inline-block; overflow:hidden; white-space:nowrap;
    border-right:2px solid var(--plasma);
    animation: typing 6s steps(42, end) infinite, caret .8s step-end infinite;
    max-width:100%;
  }
  @keyframes typing{
    0%{ width:0 }
    45%{ width:42ch }
    85%{ width:42ch }
    100%{ width:0 }
  }
  @keyframes caret{ 50%{ border-color:transparent; } }

  .links{ display:flex; gap:10px; margin-top:var(--space-5); flex-wrap:wrap; }
  .links a{
    text-decoration:none; color:var(--starlight);
    border:1px solid var(--line); background:var(--void);
    padding:7px 14px; border-radius:var(--radius-sm);
    font-size:12.5px; display:flex; align-items:center; gap:6px;
    transition:border-color .2s ease, transform .2s ease;
  }
  .links a:hover{ border-color:var(--ion); transform:translateY(-1px); }
  .links a:focus-visible{ outline:2px solid var(--ion); outline-offset:2px; }

  /* ===== STREAK ===== */
  .panel{
    margin-top:var(--space-5);
    background:linear-gradient(180deg, var(--nebula), var(--nebula-2));
    border:1px solid var(--line);
    border-radius:var(--radius-lg);
    box-shadow:var(--shadow);
    padding:var(--space-5) var(--space-6);
  }
  .panel h2{
    font-size:12px; text-transform:uppercase; letter-spacing:.08em;
    color:var(--mist); margin:0 0 var(--space-4); font-weight:600;
  }
  .streak-row{ display:flex; align-items:center; gap:var(--space-6); flex-wrap:wrap; }
  .streak-count{
    font-size:38px; font-weight:600; color:var(--solar);
  }
  .streak-count span{ font-size:14px; color:var(--mist); margin-left:6px; }
  .pulse-line{ flex:1; min-width:220px; }
  .pulse-line svg{ width:100%; height:44px; display:block; }
  .pulse-path{
    fill:none; stroke:var(--plasma); stroke-width:2;
    stroke-linecap:round; stroke-linejoin:round;
    stroke-dasharray:400; stroke-dashoffset:400;
    animation: draw 3.2s ease-in-out infinite;
  }
  @keyframes draw{
    0%{ stroke-dashoffset:400; }
    50%{ stroke-dashoffset:0; }
    100%{ stroke-dashoffset:-400; }
  }

  /* ===== SKILLS ===== */
  .group{ margin-top:var(--space-6); }
  .group h3{
    font-size:12px; text-transform:uppercase; letter-spacing:.08em;
    color:var(--mist); margin:0 0 var(--space-3); font-weight:600;
  }
  .badges{ display:flex; flex-wrap:wrap; gap:10px; }

  /* Badge 1: Core Signal — solid, primary/proven skills */
  .badge--core{
    display:inline-flex; align-items:center; gap:7px;
    padding:8px 16px; border-radius:var(--radius-sm);
    background:linear-gradient(135deg, var(--ion), var(--plasma));
    color:#0A0E1A; font-weight:600; font-size:13px;
    box-shadow:0 8px 20px -10px var(--ion-soft);
  }

  /* Badge 2: Exploring — outline + live pulse, in-progress skills */
  .badge--exploring{
    display:inline-flex; align-items:center; gap:8px;
    padding:7px 15px; border-radius:var(--radius-sm);
    border:1px solid var(--line); background:var(--void);
    color:var(--starlight); font-size:13px; font-weight:500;
  }
  .badge--exploring .live-dot{
    width:6px; height:6px; border-radius:50%; background:var(--solar);
    animation:pulseDot 1.8s infinite;
  }

  /* Badge 3: Mission — hex node, flagship projects */
  .badge--mission{
    --hex-bg: var(--nebula-2);
    position:relative; display:inline-flex; align-items:center; gap:10px;
    padding:12px 18px 12px 16px;
    clip-path: polygon(14px 0, 100% 0, 100% calc(100% - 14px), calc(100% - 14px) 100%, 0 100%, 0 14px);
    background:var(--hex-bg); border:1px solid var(--line);
    color:var(--starlight); font-size:13.5px; font-weight:600;
    text-decoration:none;
    box-shadow:0 0 0 1px transparent;
    transition:box-shadow .25s ease, transform .25s ease;
  }
  .badge--mission:hover{
    box-shadow:0 0 0 1px var(--ion), 0 12px 26px -12px var(--ion-soft);
    transform:translateY(-2px);
  }
  .badge--mission .tag{
    font-size:9.5px; text-transform:uppercase; letter-spacing:.08em;
    color:var(--plasma); display:block; margin-bottom:2px; font-weight:600;
  }

  .legend{
    margin-top:var(--space-5); display:flex; gap:var(--space-5); flex-wrap:wrap;
    font-size:12px; color:var(--mist);
  }
  .legend span{ display:flex; align-items:center; gap:6px; }
  .legend i{ width:10px; height:10px; border-radius:3px; display:inline-block; }

  footer{
    text-align:center; margin-top:var(--space-6); color:var(--mist); font-size:12px;
  }

  @media (max-width: 640px){
    .hero{ flex-direction:column; align-items:flex-start; }
    .typeline{ animation:none; width:auto; border-right:none; white-space:normal; }
    .console, .panel{ padding:var(--space-5); }
    .streak-count{ font-size:30px; }
  }

  @media (prefers-reduced-motion: reduce){
    .orbit-ring, .status .dot, .live-dot, .pulse-path, .typeline{ animation:none !important; }
  }
</style>
</head>
<body>
<div class="wrap">

  <div class="console">
    <div class="topbar">
      <div class="status"><span class="dot"></span> Mission Control — Online</div>
      <div class="toggle" role="group" aria-label="Theme toggle">
        <button id="btn-dark" class="active" aria-pressed="true" aria-label="Dark theme">🌙</button>
        <button id="btn-light" aria-pressed="false" aria-label="Light theme">☀️</button>
      </div>
    </div>

    <div class="hero">
      <div class="orbit-wrap" aria-hidden="true">
        <div class="orbit-ring"><div class="orbit-node"></div></div>
        <div class="orbit-ring r2"></div>
        <div class="avatar">AS</div>
      </div>
      <div class="heading">
        <h1 class="display">Aniket Singh</h1>
        <p class="role">B.Tech CS Student · UI &amp; AI Explorer</p>
        <span class="typeline mono">if (brain_empty) { search(StackOverflow); }</span>
      </div>
    </div>

    <div class="links">
      <a href="#" aria-label="LinkedIn profile">🔗 LinkedIn</a>
      <a href="#" aria-label="Instagram profile">📸 Instagram</a>
      <a href="#" aria-label="Email Aniket">✉️ Email</a>
    </div>
  </div>

  <div class="panel">
    <h2>Commit Signal</h2>
    <div class="streak-row">
      <div class="streak-count mono">47<span>day streak</span></div>
      <div class="pulse-line" aria-hidden="true">
        <svg viewBox="0 0 400 44" preserveAspectRatio="none">
          <path class="pulse-path" d="M0,22 L40,22 L55,6 L70,38 L85,14 L100,22 L160,22 L175,10 L190,32 L205,22 L400,22"/>
        </svg>
      </div>
    </div>
  </div>

  <div class="group">
    <h3>Core Signal — proven stack</h3>
    <div class="badges">
      <span class="badge--core">Python</span>
      <span class="badge--core">Java</span>
      <span class="badge--core">C</span>
      <span class="badge--core">TensorFlow</span>
      <span class="badge--core">HTML / CSS</span>
    </div>
  </div>

  <div class="group">
    <h3>Exploring — currently learning</h3>
    <div class="badges">
      <span class="badge--exploring"><span class="live-dot"></span>Prompt Engineering</span>
      <span class="badge--exploring"><span class="live-dot"></span>Neural Networks</span>
      <span class="badge--exploring"><span class="live-dot"></span>Streamlit</span>
    </div>
  </div>

  <div class="group">
    <h3>Mission Log — flagship builds</h3>
    <div class="badges">
      <a class="badge--mission" href="#"><span><span class="tag">Active</span>AAPDA-MITRA — flood prediction dashboard</span></a>
      <a class="badge--mission" href="#"><span><span class="tag">Polishing</span>ResuSmart — ATS resume builder</span></a>
      <a class="badge--mission" href="#"><span><span class="tag">Extending</span>Voice Assistant</span></a>
    </div>
  </div>

  <div class="legend">
    <span><i style="background:linear-gradient(135deg, var(--ion), var(--plasma));"></i>Core Signal — mastered</span>
    <span><i style="background:var(--void); border:1px solid var(--line);"></i>Exploring — in progress</span>
    <span><i style="background:var(--nebula-2); border:1px solid var(--line);"></i>Mission — flagship project</span>
  </div>

  <footer class="mono">System Compiled Successfully. ⭐ Theme-aware · keyboard-operable · reduced-motion safe.</footer>
</div>

<script>
  const root = document.documentElement;
  const btnDark = document.getElementById('btn-dark');
  const btnLight = document.getElementById('btn-light');
  function setTheme(theme){
    if(theme === 'light'){ root.setAttribute('data-theme','light'); }
    else { root.removeAttribute('data-theme'); }
    btnDark.classList.toggle('active', theme !== 'light');
    btnLight.classList.toggle('active', theme === 'light');
    btnDark.setAttribute('aria-pressed', theme !== 'light');
    btnLight.setAttribute('aria-pressed', theme === 'light');
  }
  btnDark.addEventListener('click', () => setTheme('dark'));
  btnLight.addEventListener('click', () => setTheme('light'));
</script>
</body>
</html>
