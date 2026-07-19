def load_css():
    return """
<style>

/* ==============================
   Global
================================ */

.main > div {
    padding-top: 1rem;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}

/* ==============================
   Title
================================ */

h1 {
    color: #2563eb;
    font-weight: 700;
}

h2 {
    color: #1e40af;
}

h3 {
    color: #1d4ed8;
}

/* ==============================
   Cards
================================ */

div[data-testid="stVerticalBlock"] > div {
    border-radius: 12px;
}

/* ==============================
   Metric Cards
================================ */

div[data-testid="metric-container"] {
    background-color: #f8fafc;
    border: 1px solid #e5e7eb;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 2px 6px rgba(0,0,0,.05);
}

/* ==============================
   Buttons
================================ */

.stButton>button {

    width:100%;

    border-radius:10px;

    height:45px;

    background:#2563eb;

    color:white;

    font-weight:bold;

    border:none;

}

.stButton>button:hover{

    background:#1d4ed8;

    color:white;

}

/* ==============================
   Download Buttons
================================ */

.stDownloadButton>button{

    width:100%;

    border-radius:10px;

}

/* ==============================
   Sidebar
================================ */

section[data-testid="stSidebar"]{

    background:#f8fafc;

}

/* ==============================
   Tables
================================ */

table {

    border-collapse:collapse;

}

th{

    background:#2563eb;

    color:white;

}

td,th{

    padding:10px;

}

/* ==============================
   JSON
================================ */

pre{

    border-radius:10px;

}

/* ==============================
   Success
================================ */

div[data-baseweb="notification"]{

    border-radius:10px;

}

/* ==============================
   Footer
================================ */

footer{

    visibility:hidden;

}

</style>
"""