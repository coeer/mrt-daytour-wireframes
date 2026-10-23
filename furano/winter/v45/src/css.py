# -*- coding: utf-8 -*-
CSS = r'''
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:780px}
body{background:#eef2f6;color:#22303d;
 font-family:"Noto Sans SC","Noto Sans KR","Microsoft YaHei","Malgun Gothic",sans-serif;
 -webkit-font-smoothing:antialiased;font-size:15px;line-height:1.72}
img{display:block;width:100%;height:100%;object-fit:cover}
.page{width:780px;overflow:hidden;background:#eef2f6}
.serif{font-family:"Cormorant Garamond",Georgia,serif}
section{position:relative}

/* ============ COVER ============ */
.cover{height:900px;background:#0f1e2c}
.cover .shade{position:absolute;inset:0;
 background:linear-gradient(180deg,rgba(9,22,36,.58) 0%,rgba(9,22,36,.10) 22%,rgba(9,22,36,.22) 46%,rgba(11,26,41,.92) 80%,#0c1826 100%)}
.cover .brand{position:absolute;top:0;left:24px;background:#fff;border-radius:0 0 14px 14px;
 padding:14px 22px;box-shadow:0 4px 10px rgba(15,30,44,.16),0 12px 28px rgba(15,30,44,.18);
 display:flex;align-items:center;justify-content:center}
.cover .brand img{height:40px;width:auto;object-fit:contain}
.cover .tag{position:absolute;top:34px;right:26px;color:#fff;font-size:12.5px;letter-spacing:.16em;
 padding:7px 13px;border-radius:999px;background:rgba(15,30,44,.38);backdrop-filter:blur(3px);
 text-shadow:0 1px 3px rgba(9,22,36,.5)}
.cover .txt{position:absolute;left:0;right:0;bottom:54px;text-align:center;color:#fff;padding:0 52px;display:flex;flex-direction:column;align-items:center}
.cover .eyebrow{font-size:20px;letter-spacing:.32em;color:#e8a33d;margin-bottom:14px;
 font-family:"Cormorant Garamond",Georgia,serif;font-style:italic}
.cover h1{font-size:41px;line-height:1.26;font-weight:900;letter-spacing:.01em}
.cover .sub{margin-top:12px;font-size:16.5px;color:#c6d7e6}
.cover .chips{margin-top:22px;display:flex;justify-content:center;gap:9px;flex-wrap:wrap}
.cover .chips span{font-size:12.5px;padding:6px 13px;border-radius:999px;
 background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.34);color:#eaf2f9;backdrop-filter:blur(2px)}

/* ============ DECIDE ============ */
.decide{background:#0f1e2c;padding:0 38px 46px}
.dcard{background:#fff;border-radius:22px;padding:30px 26px 24px;box-shadow:0 14px 34px rgba(4,14,24,.28)}
.dcard .q{font-size:21px;font-weight:900;text-align:center;line-height:1.45}
.dcard .q em{font-style:normal;color:#8a6cae}
.dcard .qnote{text-align:center;font-size:13px;color:#8b9aa8;margin:6px 0 22px}
.opt{display:flex;align-items:center;gap:15px;border-radius:16px;padding:15px 16px;margin-bottom:11px;position:relative}
.opt .lb{width:40px;height:40px;border-radius:50%;color:#fff;font-weight:900;font-size:19px;
 display:flex;align-items:center;justify-content:center;flex:0 0 40px}
.opt .tx{flex:1}
.opt .tx b{display:block;font-size:16px;font-weight:800;letter-spacing:.01em}
.opt .tx i{font-style:normal;font-size:13px;color:#7c8b99;display:block;margin-top:2px}
.opt .flag{position:absolute;top:-9px;right:14px;background:#f3c440;color:#5c4405;
 font-size:11.5px;font-weight:900;padding:3px 10px;border-radius:999px;letter-spacing:.04em}
.opt.a{background:#f5f0fa}.opt.a .lb{background:#8a6cae}
.opt.b{background:#fdf3ec}.opt.b .lb{background:#d4763f}
.opt.c{background:#f0f7f2}.opt.c .lb{background:#3f7d55}
.cmp{display:flex;gap:9px;margin-top:20px}
.cmp div{flex:1;text-align:center;border:1px solid #e3e9ef;border-radius:14px;padding:13px 6px;background:#fafcfe}
.cmp b{display:block;font-size:13.5px;font-weight:800;margin-bottom:5px}
.cmp span{display:block;font-size:11.5px;color:#7f8e9c;line-height:1.55}
.cmp .ca b{color:#7a5fa1}.cmp .cb b{color:#c26c36}.cmp .cc b{color:#357049}

/* ============ COURSE ============ */
.coursewrap{padding:22px 38px}
.card{background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 4px 16px rgba(20,40,60,.06)}
.chead{padding:26px 26px 0;display:flex;gap:15px;align-items:flex-start}
.chead .badge{flex:0 0 46px;width:46px;height:46px;border-radius:13px;color:#fff;font-weight:900;font-size:23px;
 display:flex;align-items:center;justify-content:center;box-shadow:0 6px 14px rgba(20,40,60,.16)}
.chead h2{font-size:23px;font-weight:900;line-height:1.32}
.chead h2 em{font-style:normal;font-size:15px;font-weight:800;color:#fff;padding:3px 9px;border-radius:8px;margin-left:4px;vertical-align:3px};display:inline-block;margin-top:4px
.chead .cs{font-size:13.5px;color:#7c8b99;margin-top:7px}
.tagline{margin:18px 26px 0;text-align:center;font-size:19px;letter-spacing:.26em;font-weight:600;
 font-family:"Cormorant Garamond",Georgia,serif;color:#a8b6c4;padding:11px 0;border-top:1px solid #edeff3;border-bottom:1px solid #edeff3}
.intro{margin:18px 26px 0;font-size:14.5px;line-height:1.85;color:#3b4a58;background:#fafbfd;
 border-radius:14px;padding:17px 18px;border-left:4px solid #dfe6ee}
.intro .lead{display:block;margin-bottom:5px}
.tip{margin:13px 26px 0;font-size:13px;color:#6d7c8b;line-height:1.7}
.tip b{color:#4a5a69}
figure{margin:18px 26px 0;border-radius:15px;overflow:hidden;position:relative;background:#dde5ec}
figure .cap{position:absolute;left:0;right:0;bottom:0;padding:22px 15px 11px;color:#fff;font-size:12.5px;
 background:linear-gradient(180deg,rgba(8,20,32,0),rgba(8,20,32,.78))}
.f2{display:flex;gap:11px;margin:13px 42px 0}
.f2 figure{margin:0;flex:1;display:flex;flex-direction:column}
.f2 figure img{height:158px;width:100%;object-fit:cover;border-radius:11px 11px 0 0}
.f2 figure .cap{position:static;padding:7px 4px 3px;font-size:11px;background:none;color:#5a6a78;text-align:center}
.tl{position:relative;margin:24px 42px 6px}
.tl:before{content:"";position:absolute;left:72px;top:8px;bottom:4px;border-left:2px dotted #cdd8e4}
.ev{position:relative;padding-left:98px;margin-bottom:21px}
.ev:last-child{margin-bottom:6px}
.ev .pill{position:absolute;left:0;top:0;width:62px;height:48px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-size:11.5px;font-weight:900;line-height:1.4;border-radius:9px;letter-spacing:.02em;padding:4px 2px}
.ev .time{position:absolute;left:0;top:21px;width:60px;text-align:center;font-size:12.5px;font-weight:900;color:#455666}
.ev .dot{position:absolute;left:65px;top:9px;width:15px;height:15px;border-radius:50%;background:#fff;
 border:3.4px solid #b9c6d3;box-sizing:border-box}
.ev h4{font-size:15.5px;font-weight:900;line-height:1.5}
.ev h4 .dur{font-size:12.5px;font-weight:600;color:#8b9aa8;margin-left:2px}
.ev p{font-size:13.8px;color:#4d5d6d;line-height:1.8;margin-top:5px}
.ev.hl .dot{border-color:#f3c440;background:#f3c440;box-shadow:0 0 0 4px rgba(243,196,64,.22)}
.star{display:inline-block;background:#f3c440;color:#5c4405;font-size:11px;font-weight:900;
 padding:2px 8px;border-radius:999px;margin-left:6px;vertical-align:2px}
.ev.hl{background:linear-gradient(90deg,rgba(243,196,64,.13),rgba(243,196,64,0) 78%);
 border-radius:12px;padding-top:10px;padding-bottom:12px;margin-top:-4px}
.ev.hl h4{color:#8a6410}
.ev.plain .dot{border-color:#c9d5e1}
.ev.plain .pill{background:#f1f4f7;color:#7f8e9c}
.notice{margin:6px 26px 42px;border-radius:14px;padding:15px 17px;font-size:13px;line-height:1.78;color:#5a6a78;background:#f4f7fa}
.notice b{color:#3c4b59}
.notice.warn{margin-top:0}

.ctag{display:inline-block;font-size:13.5px;font-weight:800;color:#fff;padding:4px 11px;border-radius:8px;margin-top:9px;background:#3a6ea5}

/* course colors */
.A{--c:#3a6ea5}
.B{--c:#d4763f}
.C{--c:#3f7d55}
.A .badge{background:#3a6ea5}
.B .badge{background:#d4763f}
.C .badge{background:#3f7d55}
.A .chead h2 em{background:#3a6ea5}
.B .chead h2 em{background:#d4763f}
.C .chead h2 em{background:#3f7d55}
.A .tl:before{border-color:#cfdfef}.A .ev .pill{background:#ecf4fb;color:#2c5a8a}
.B .tl:before{border-color:#f2d6c3}.B .ev .pill{background:#fdf1e9;color:#a85a28}
.C .tl:before{border-color:#cfe3d5}.C .ev .pill{background:#eef7f1;color:#2f6a45}

/* ============ HOOK（痛点三难，冬季版新增） ============ */
.hook{background:#0f1e2c;padding:6px 38px 40px}
.hkcard{background:#fff;border-radius:22px;padding:28px 26px 24px;box-shadow:0 14px 34px rgba(4,14,24,.28)}
.hkq{font-size:21px;font-weight:900;text-align:center;line-height:1.45;color:#22303d;margin-bottom:18px}
.hkline{display:flex;gap:13px;align-items:flex-start;padding:11px 4px;border-top:1px dashed #e6ecf2}
.hkline:first-of-type{border-top:none}
.hkic{flex:0 0 64px;font-size:13px;font-weight:900;color:#8b9aa8;text-align:center;padding-top:2px}
.hktx{flex:1;font-size:13.8px;line-height:1.75;color:#4d5d6d}
.hkans{margin-top:16px;background:#fdf3ec;border-left:4px solid #d4763f;border-radius:12px;
 padding:15px 17px;font-size:14.5px;line-height:1.75;color:#3b4a58}
.hkans b{color:#c26c36}

/* hook intro 段 */
.hkintro{font-size:14px;line-height:1.85;color:#3b4a58;background:#fafbfd;
 border-radius:14px;padding:16px 18px;border-left:4px solid #3a6ea5;margin-bottom:14px}

/* 费用含/不含 */
.cost-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.cost-box{background:#fff;border:1px solid #e3ebf5;border-radius:16px;padding:18px 20px 14px}
.cost-box h5{font-size:15px;font-weight:900;margin-bottom:9px}
.cost-box.inc h5{color:#2e6b4f}.cost-box.exc h5{color:#a05454}
.cost-box ul{margin:0;padding:0}
.cost-box li{font-size:12.8px;line-height:1.75;color:#4d5d6d;list-style:none;
 padding-left:16px;position:relative;margin-top:6px}
.cost-box.inc li:before{content:"✓";position:absolute;left:0;color:#2e6b4f;font-weight:900}
.cost-box.exc li:before{content:"–";position:absolute;left:0;color:#a05454;font-weight:900}

/* ============ BREATH (路线收尾 -> 横幅 呼吸带) ============ */
.breath{background:#eef2f6;text-align:center;padding:28px 0 0}
.breath .t{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;
 font-size:17px;letter-spacing:.3em;color:#93a3b2;display:flex;align-items:center;
 justify-content:center;gap:16px}
.breath .t:before,.breath .t:after{content:'';width:64px;height:1px;background:#ccd7e2}

/* ============ BAND ============ */
.bandimg{height:300px;position:relative;overflow:hidden;background:#0f1e2c}
.bandimg:before{content:'';position:absolute;left:0;right:0;top:0;height:110px;z-index:1;
 background:linear-gradient(180deg,#eef2f6 0%,rgba(238,242,246,.55) 45%,rgba(238,242,246,0) 100%)}
.bandimg:after{content:'';position:absolute;left:0;right:0;bottom:0;height:190px;z-index:1;
 background:linear-gradient(0deg,#1d2e3e 0%,rgba(29,46,62,.6) 55%,rgba(29,46,62,0) 100%)}
.bandimg .shade{position:absolute;inset:0;
 background:linear-gradient(180deg,rgba(12,26,40,.62),rgba(12,26,40,.18) 42%,rgba(12,26,40,.72))}
.bandimg .txt{position:absolute;inset:0;z-index:2;display:flex;flex-direction:column;align-items:center;
 justify-content:center;color:#fff;text-align:center;padding:0 40px}
.bandimg .txt b{font-size:22px;font-weight:900;letter-spacing:.02em;text-shadow:0 2px 12px rgba(0,0,0,.5)}
.bandimg .txt span{font-size:12.5px;color:#e2ecf4;margin-top:9px;letter-spacing:.04em;text-shadow:0 1px 8px rgba(0,0,0,.5)}

/* ============ TRUST ============ */
.trust{background:#0f1e2c;padding:40px 38px 44px;color:#fff}
.trust .th{text-align:center;padding:0 12px 26px}
.trust .th .k{font-size:12px;letter-spacing:.3em;color:#8fa6ba;margin-bottom:12px}
.trust .th h3{font-size:20px;line-height:1.6;font-weight:900}
.trust .th h3 b{color:#f0dcae}
.tcard{background:#fff;border-radius:20px;padding:24px 22px;color:#22303d;margin-bottom:16px}
.tcard .vt{display:flex;gap:12px;align-items:baseline;margin-bottom:14px}
.tcard .vt .n{font-size:12px;font-weight:900;color:#fff;background:#22303d;border-radius:7px;padding:4px 9px}
.tcard .vt .t{font-size:16.5px;font-weight:900}
.tcard .vt .t i{font-style:normal;font-size:13px;color:#8b9aa8;font-weight:600;margin-left:6px}
.vcols{display:flex;gap:13px;margin-bottom:11px}
.vcols .vbig{flex:1;height:200px;border-radius:13px;overflow:hidden;background:#fff;border:1px solid #eef2f6}
.vcols .vside{flex:0 0 272px;height:200px;border-radius:13px;overflow:hidden;background:#e9eef3}
.vlabels{display:flex;gap:13px;margin:-4px 0 6px;font-size:11.5px;color:#9aa8b5;font-weight:700}
.vlabels span:first-child{flex:1}
.vlabels span:last-child{flex:0 0 272px;text-align:center}
.vlabels span:first-child{text-align:center}
.seatwrap{margin-top:15px}
.seatwrap .map{background:#f5f8fb;border:1px solid #e9eef4;border-radius:15px;
 padding:13px 16px 9px;max-width:352px;margin:0 auto}
.seatwrap .cap{display:flex;justify-content:space-between;align-items:center;
 font-size:11.5px;color:#8b9aa8;font-weight:700;margin-bottom:10px}
.seatwrap .cap b{color:#22303d;font-size:11.5px;background:#fff;border:1px solid #e6ecf2;
 border-radius:999px;padding:3px 11px;font-weight:800}
.seatwrap .map svg{max-width:232px;margin:0 auto;display:block}
.seatwrap .foot{text-align:center;font-size:10.5px;color:#a7b3c0;margin-top:6px}
.certcard{background:#fff;border-radius:20px;padding:20px 22px;color:#22303d}
.certflex{display:flex;gap:14px;align-items:stretch;margin-bottom:16px}
.certflex .cimg{flex:0 0 188px;border-radius:12px;overflow:hidden;background:#f6f4ee;border:1px solid #efe9dd}
.certflex .cwide{flex:1;border-radius:12px;overflow:hidden;background:#e9eef3}
.certtx b{display:block;font-size:15px;font-weight:900;line-height:1.55;margin-bottom:8px}
.certtx p{font-size:13.2px;line-height:1.8;color:#4d5d6d}
.certtx .capp{margin-top:9px;display:inline-block;font-size:11.5px;font-weight:800;
 color:#8a6a1e;background:#fbf3dd;border-radius:999px;padding:4px 11px}

/* ============ PICKUP ============ */
.pickup{padding:0}
.pband{background:linear-gradient(135deg,#2b6fb5,#3f8fce);color:#fff;text-align:center;padding:30px 20px}
.pband .k{font-size:12px;letter-spacing:.34em;opacity:.8}
.pband h3{font-size:23px;font-weight:900;margin-top:9px}
.pband p{font-size:13px;opacity:.9;margin-top:7px}
.pcard{background:#fff;margin:22px 38px;border-radius:22px;padding:24px 22px;box-shadow:0 4px 16px rgba(20,40,60,.06)}
.pcard h4{font-size:16px;font-weight:900;text-align:center;margin-bottom:5px}
.pcard .pnote{font-size:12.5px;color:#8b9aa8;text-align:center;margin-bottom:16px}
.mapbox{border-radius:15px;overflow:hidden;background:#e8eff7;border:1px solid #e0e8f0}
.legend{display:flex;justify-content:center;gap:20px;margin-top:13px;font-size:12px;color:#6d7c8b}
.legend i{display:inline-block;width:11px;height:11px;border-radius:3px;margin-right:6px;vertical-align:-1px}
.stop{display:flex;gap:14px;align-items:center;margin-top:16px;border:1px solid #e8eef4;border-radius:16px;padding:12px;background:#fbfcfe}
.stop .ph{flex:0 0 132px;height:92px;border-radius:12px;overflow:hidden;background:#e6ecf2}
.stop .tx b{font-size:14.5px;font-weight:900;display:block}
.stop .tx span{font-size:12.5px;color:#7c8b99;line-height:1.65;display:block;margin-top:4px}
.stop .tx em{font-style:normal;display:inline-block;margin-top:7px;font-size:11.5px;font-weight:900;
 color:#2b6fb5;background:#eaf3fc;border-radius:999px;padding:3px 10px}

/* ============ FAQ ============ */
.trustpickup{background:#1d2e3e;font-size:0;line-height:0}
.faqzone{background:#1d2e3e;padding:0 38px 46px}
.fhead{background:transparent;border-radius:0;padding:38px 2px 26px;color:#fff;display:flex;gap:13px;align-items:center}
.fhead .ic{flex:0 0 42px;height:42px;border-radius:12px;background:rgba(255,255,255,.12);display:flex;
 align-items:center;justify-content:center;font-size:20px}
.fhead b{font-size:17.5px;font-weight:900;line-height:1.45;display:block}
.fhead span{font-size:12.5px;color:#9db2c4;display:block;margin-top:3px}
.fbody{background:#fff;border-radius:22px;padding:6px 18px 20px;box-shadow:0 4px 16px rgba(20,40,60,.06)}
.qa{padding:15px 0;border-bottom:1px dashed #e6ecf2}
.qa:last-child{border-bottom:0}
.qa .q{display:flex;gap:11px;align-items:flex-start}
.qa .q .n{flex:0 0 30px;height:30px;border-radius:9px;background:linear-gradient(135deg,#4f9aa3,#6fbcc4);
 color:#fff;font-weight:900;font-size:13px;display:flex;align-items:center;justify-content:center;margin-top:1px}
.qa .q b{font-size:14.5px;font-weight:900;line-height:1.6;color:#2c4354;flex:1}
.qa .a{font-size:13.4px;line-height:1.88;color:#4d5d6d;padding-left:41px;margin-top:8px}
.qa .a em{font-style:normal;background:#eef7f6;border-radius:6px;padding:1px 6px;font-weight:700;color:#2f6c74}
.qa .a a{color:#2b6fb5;text-decoration:none;border-bottom:1px solid #bcd6ee}
.fend{margin-top:6px;background:#f4f9f8;border-radius:14px;padding:15px 18px;text-align:center;
 font-size:13.5px;color:#3c6169;font-weight:700;line-height:1.7}

/* ============ END ============ */
.end{position:relative;height:430px;background:#1d2e3e;overflow:hidden}
.end .shade{position:absolute;inset:0;background:linear-gradient(180deg,#1d2e3e 0%,rgba(29,46,62,0) 26%,rgba(9,22,36,.45) 48%,rgba(9,22,36,.9) 100%)}
.end .txt{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;padding:0 46px;text-align:center}
.end .eyebrow{font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-size:18px;letter-spacing:.3em;color:#f0dcae}
.end h3{font-size:25px;font-weight:900;margin-top:13px;line-height:1.5}
.end p{font-size:13.5px;color:#c3d3e0;margin-top:11px;line-height:1.75}
.end .line{width:52px;height:2px;background:#f0dcae;margin:18px auto 0;opacity:.7}
.copyright{background:#0b1723;color:#6e8296;text-align:center;font-size:11.5px;padding:15px 20px;line-height:1.7}
.cover img{object-position:center 28%}
.cover .sub b{color:#e8a33d;font-weight:800}
.trustpickup{background:#f2f4f7}
.seam-fade{height:44px;background:linear-gradient(180deg,#f2f4f7 0%,#e8edf3 45%,#0f1e2c 100%);margin:0}
.faq{padding-top:0}
'''



