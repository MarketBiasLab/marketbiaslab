from flask import Flask, Response, send_from_directory

app = Flask(__name__, static_folder="static", static_url_path="/static")


HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Market Bias Lab</title>
  <meta name="description" content="BTC-based market bias delivered by email. Observation only." />

  <!-- Favicon -->
  <link rel="icon" href="/favicon.ico" />

  <style>
    :root {
      --bg: #0b0f14;
      --card: #0f1620;
      --text: #e6edf3;
      --muted: #9fb0c0;
      --line: rgba(255,255,255,.10);
      --accent: #5aa9ff;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
      background: radial-gradient(1200px 600px at 20% 10%, rgba(90,169,255,.10), transparent 60%),
                  radial-gradient(1000px 700px at 80% 30%, rgba(90,255,203,.08), transparent 55%),
                  var(--bg);
      color: var(--text);
      line-height: 1.5;
    }
    a { color: var(--accent); text-decoration: none; }
    a:hover { text-decoration: underline; }

    .wrap { max-width: 980px; margin: 0 auto; padding: 28px 18px 60px; }

    .nav {
      display: flex; align-items: center; justify-content: space-between;
      gap: 12px; padding: 10px 0 22px;
    }

    .brand {
      font-weight: 700; letter-spacing: .2px;
      display: flex; gap: 10px; align-items: center;
    }
    .brand img {
      width: 110px; height: 110px;
      border-radius: 6px;
      border: 1px solid var(--line);
    }

    .links { display:flex; gap:14px; flex-wrap:wrap; font-size: 14px; color: var(--muted); }

    .hero {
      border: 1px solid var(--line);
      background: linear-gradient(180deg, rgba(255,255,255,.03), rgba(255,255,255,.01));
      border-radius: 18px;
      padding: 26px 22px;
    }

    .heroHeader {
      width: 100%;
      border-radius: 14px;
      border: 1px solid var(--line);
      margin-bottom: 16px;
      display: block;
    }

    h1 { margin: 0 0 10px; font-size: 34px; letter-spacing: -0.4px; }
    .sub { margin: 0 0 16px; color: var(--muted); font-size: 16px; max-width: 820px; }

    .pillrow { display:flex; gap:10px; flex-wrap: wrap; margin-top: 14px; }
    .pill {
      border: 1px solid var(--line);
      padding: 7px 10px;
      border-radius: 999px;
      font-size: 13px;
      color: var(--muted);
      background: rgba(255,255,255,.02);
    }

    .grid { display:grid; grid-template-columns: repeat(12, 1fr); gap: 14px; margin-top: 16px; }
    .card {
      grid-column: span 4;
      border: 1px solid var(--line);
      background: rgba(255,255,255,.02);
      border-radius: 16px;
      padding: 16px 16px;
    }
    .card h3 { margin: 0 0 6px; font-size: 16px; }
    .card p { margin: 0; color: var(--muted); font-size: 14px; }
    @media (max-width: 860px) { .card { grid-column: span 12; } }

    section { margin-top: 22px; }
    .sectionTitle { font-size: 18px; margin: 0 0 10px; }

    .steps { display:grid; grid-template-columns: repeat(12, 1fr); gap: 14px; }
    .step {
      grid-column: span 4;
      border: 1px solid var(--line);
      border-radius: 16px;
      padding: 16px;
      background: rgba(255,255,255,.02);
    }
    @media (max-width: 860px) { .step { grid-column: span 12; } }

    .k { color: var(--muted); font-size: 13px; margin-bottom: 6px; }
    .v { font-weight: 650; margin: 0 0 6px; }

    .sample {
      border: 1px solid var(--line);
      border-radius: 16px;
      background: rgba(255,255,255,.02);
      padding: 16px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      color: #d9e3ef;
      font-size: 13px;
      white-space: pre-wrap;
    }

    .faq { border: 1px solid var(--line); border-radius: 16px; background: rgba(255,255,255,.02); padding: 16px; }
    details { border-top: 1px solid var(--line); padding: 10px 0; }
    details:first-of-type { border-top: none; }
    summary { cursor: pointer; font-weight: 650; }
    .ans { color: var(--muted); margin-top: 8px; }

    footer {
      margin-top: 22px;
      color: var(--muted);
      font-size: 13px;
      border-top: 1px solid var(--line);
      padding-top: 16px;
    }
    .contact { display:flex; gap:10px; flex-wrap:wrap; align-items:center; }
    .muted { color: var(--muted); }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="nav">
      <div class="brand">
        <img src="/static/MBL_logo.png" alt="Market Bias Lab logo" />
        <span>Market Bias Lab</span>
      </div>
      <div class="links">
        <a href="#what">What you get</a>
        <a href="#how">How it works</a>
        <a href="#sample">Sample</a>
        <a href="#access">Access</a>
        <a href="#faq">FAQ</a>
      </div>
    </div>

    <div class="hero">
      <img class="heroHeader" src="/static/MBL_header.png" alt="Market Bias Lab header" />

      <h1>BTC-based market bias. Delivered by email.</h1>
      <p class="sub">
        Market Bias Lab provides <strong>directional market context for observation only</strong>—derived from Bitcoin price structure using a single, consistent framework.
      </p>

      <div class="pillrow">
        <div class="pill">No trade signals</div>
        <div class="pill">No entries</div>
        <div class="pill">No investment advice</div>
        <div class="pill">Low frequency (max 1–2/day)</div>
        <div class="pill">Email-first</div>
      </div>

      <div class="grid" id="what">
        <div class="card">
          <h3>Daily Market Bias</h3>
          <p>Daily BTC-based market bias: <strong>Bullish</strong> or <strong>Bearish</strong>.</p>
        </div>
        <div class="card">
          <h3>Low Frequency</h3>
          <p>Max <strong>1–2 updates/day</strong>. If bias doesn’t change, no update will be sent.</p>
        </div>
        <div class="card">
          <h3>Email First</h3>
          <p>Delivered by email for clarity, consistency, and minimal noise.</p>
        </div>
      </div>
    </div>

    <section id="how">
      <h2 class="sectionTitle">How it works</h2>
      <div class="steps">
        <div class="step">
          <div class="k">Step 1</div>
          <div class="v">Read Structure</div>
          <div class="muted">Bias is derived from <strong>Bitcoin price structure</strong> using a single structural condition.</div>
        </div>
        <div class="step">
          <div class="k">Step 2</div>
          <div class="v">Publish Bias</div>
          <div class="muted">We publish a simple directional context: <strong>Bullish</strong> or <strong>Bearish</strong>.</div>
        </div>
        <div class="step">
          <div class="k">Step 3</div>
          <div class="v">You Decide</div>
          <div class="muted">You decide whether and how to use it. We do not provide trade instructions.</div>
        </div>
      </div>
    </section>

    <section id="sample">
      <h2 class="sectionTitle">Sample format</h2>
      <div class="sample">
Subject: BTC-based market bias: Bearish
Body:
Today’s BTC-based market bias: Bearish.
Observation only.

---

Subject: Market bias unchanged
Body:
Market bias unchanged.
No rush. Observation only.
      </div>
    </section>

    <section id="access">
      <h2 class="sectionTitle">Access</h2>
      <div class="faq">
        <p style="margin:0 0 8px;">
          Market Bias Lab is currently in a <strong>limited-access phase</strong>.
        </p>
        <p style="margin:0;">
          Subscription details will be announced at a later stage. If you are interested in early access, please follow our updates on X.
        </p>
      </div>
    </section>

    <section id="faq">
      <h2 class="sectionTitle">FAQ</h2>
      <div class="faq">
        <details open>
          <summary>Is this a trading signal service?</summary>
          <div class="ans">
            No. Market Bias Lab provides directional market context for observation only. We do not provide trade signals, entries, exits, targets, or investment advice.
          </div>
        </details>
        <details>
          <summary>What market is this based on?</summary>
          <div class="ans">The bias is derived from <strong>Bitcoin price structure</strong>.</div>
        </details>
        <details>
          <summary>How often will I receive emails?</summary>
          <div class="ans">Up to <strong>1–2 times per day</strong>. If there is no change, no email will be sent.</div>
        </details>
        <details>
          <summary>Do you offer trading support or coaching?</summary>
          <div class="ans">No. This service does not provide individual trading support or strategy guidance.</div>
        </details>
        <details>
          <summary>Do you guarantee performance?</summary>
          <div class="ans">No. This is an observational framework, not a performance product.</div>
        </details>
      </div>
    </section>

    <footer>
      <div style="margin-bottom:10px;">
        <strong>Disclaimer:</strong> Market Bias Lab is an informational service for market observation only and does not provide investment advice. Trading and investing involve risk. You are solely responsible for your decisions.
      </div>
      <div class="contact">
        <span>Contact:</span> <a href="mailto:support@marketbiaslab.com">support@marketbiaslab.com</a>
      </div>
    </footer>
  </div>
</body>
</html>
"""

@app.get("/")
def home():
    return Response(HTML, mimetype="text/html; charset=utf-8")

@app.get("/favicon.ico")
def favicon():
    # Uses your existing logo as favicon to avoid /favicon.ico 404
    return send_from_directory("static", "MBL_logo.png")

if __name__ == "__main__":
    # Run locally: http://127.0.0.1:5000
    app.run(host="0.0.0.0", port=5000, debug=True)
