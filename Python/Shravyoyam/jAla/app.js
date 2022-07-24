var hide = (e = "pack") => $l("#" + e).hide(),
    show = (e = "pack") => {
        $l("#" + e).show();
        if ("pack" == e) {
            $l("#abhitodanam").css("background-color", "white");
            setTimeout(() => $l("#abhitodanam").css("background-color", "black"), 500);
        }
    },
    blink = () => {
        show("blink");
        setTimeout(() => hide("blink"), 400)
    },
    kRyate = () => {
        let e = $l("#lekh").val();
        $l("#nirdhAraNa").hide();
        if (e == "")
            return;
        store.setItem("sthAnam", e);
    },
    kRyate1 = () => {
        let e = $l("#dtl");
        e.show();
        e.html(store.getItem("sthAnam"));
        e.append("<br><br>" + JSON.stringify(data));
    };
$l("#abhitodanam").on("input", function () {
    if (lasan) {
        key_num++;
        setTimeout(() => {
            if (key_num == 0)
                return;
            else if (key_num == 1)
                this.value = "";
            key_num--;
        }, 3000)
    } else
        this.value = "";
});
$l("#abhitodanam").on("keydown", () => {
    if (lasan && 13 == (event.keyCode || event.which)) {
        collect = [];
        todana_niyantraNa(1);
    }
});
$l("#dvayam").on("click", () => todana_niyantraNa(2));
$l("#ekam").on("click", () => todana_niyantraNa(1));
$l("#dvayam").on("dblclick", () => {
    if (chalitam) {
        lasan = false;
        $l("#su div.mdi").html("");
        $l(".cntrl1").hide();
        hide();
    }
});
$l("#ekam").on("dblclick", () => {
    if (chalitam) {
        hide()
        let e = $l("#su");
        if (null == e || null == e) return;
        let t = e.css("visibility"),
            l = ["visible", "hidden"];
        e.css("visibility", l[Math.abs(l.indexOf(t) - 1)])
    }
});
$l("#show_1").on("click", () => {
    $l(".cntrl, #hide_1").show();
    $l("#show_1").hide();
})
$l("#hide_1").on("click", () => {
    $l(".cntrl, #hide_1").hide();
    $l("#show_1").show();
})
$l("#load_current").on("click", () => {
    let dur = $l("#media")[0].currentTime;
    let sec = dur % 60;
    dur -= sec;
    dur /= 60;
    sec = parseInt(sec);
    let min = dur % 60;
    dur -= min;
    dur /= 60;
    let hrs = dur % 60;
    $l("#secs").val(sec)
    $l("#mins").val(min)
    $l("#hrs").val(hrs)
})
$l("#set_current").on("click", () => {
    let t = parseInt($l("#secs").val())
    t += parseInt($l("#mins").val()) * 60
    t += parseInt($l("#hrs").val()) * 3600
    $l("#media")[0].currentTime = t;
})
$l("#lower_time").on("click", () => {
    let dur = $l("#media")[0].currentTime;
    dur -= 10;
    $l("#media")[0].currentTime = dur;
    $l("#load_current").trigger("click")
})
$l("#higher_time").on("click", () => {
    let dur = $l("#media")[0].currentTime;
    dur += 10;
    $l("#media")[0].currentTime = dur;
    $l("#load_current").trigger("click")
})
var collect = [],
    chalitam = false,
    lasan = false,
    key_num = 0;
hide();
var todana_niyantraNa = (e => {
    collect.push(e);
    if (lasan && 1 == e && 1 == collect.length && loaded) {
        let vl = $l("#abhitodanam").val();
        if (!(!(vl in data) || $l("#abhitodanam").val() == "")) {
            let e = data[vl],
                a = ["audio", "video"][e[2]],
                n = `<${a} controls loop autoplay id="media"><source src="${store.getItem("sthAnam")+(l="/"+e[0])}"></${a}>`;
            $l("#su div.mdi").html(n);
            $l("#su").css("visibility", "hidden")
            $l(".cntrl1").show();
            $l("#sUchI").val(vl)
            lasan = false;
            hide();
        }
        $l("#abhitodanam").val("");
        if (vl != "")
            collect = [];
    }
    let jn = collect.join("");
    if (chalitam) {
        if ("12" == jn) {
            lasan = true;
            show();
        } else if ("21" == jn) {
            chalitam = false;
            lasan = false;
            $l("#su div.mdi").html("");
            $l(".cntrl1").hide();
            hide();
        }
        if (jn.length == 2) {
            collect = [];
            blink();
        }
    } else if ("22112" == jn) {
        $l("#bdy").css("background-color", "purple");
        setTimeout(() => $l("#bdy").css("background-color", "black"), 500);
        chalitam = true;
    } else if ("11211" == jn)
        show("nirdhAraNa")
    if (5 == jn.length) {
        collect = [];
        blink();
    }
});
var store = window.localStorage,
    loaded = false;
if ("sthAnam" in store) {
    // in android begin with file:///storage
    // also allow file permision manualy
    $lf.getScript(store.getItem("sthAnam") + "/saYc.js", () => {
        let ht = "";
        for (let x in data)
            ht += `<option value="${x}">${data[x][1]} :- ${x} ${["🎵","📀"][data[x][2]]}</option>`;
        $l("#sUchI").html(ht);
        $l("#sUchI").on("change", function () {
            $l("#abhitodanam").val(this.value);
            collect = [];
            todana_niyantraNa(1);
        })
    });
    loaded = true;
} else $l("#bdy").css("background-color", "#361e1e");
$l(".sam").on("click", function () {
    let e = $l(this);
    e.css("border-color", "blue");
    setTimeout(() => e.css("border-color", ""), 100)
});
$l(".sam").on("dblclick", function () {
    let e = $l(this);
    e.css("border-color", "red");
    setTimeout(() => e.css("border-color", ""), 100)
});