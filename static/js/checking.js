async function checkDomain() {
    try {
        const res = await fetch('/check');
        const data = await res.json();

        if (data.ok) {
            window.location.href = data.url;
        } else {
            window.location.href = "/error";
        }
    } catch (e) {
        window.location.href = "/error";
    }
}

checkDomain();
