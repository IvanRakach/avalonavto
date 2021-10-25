/* Значения из input radio */ // ---> посмотреть https://qna.habr.com/q/620323
// 1. Категория клиента: ФЛ или ЮЛ
var customersType = document.getElementsByName('customers_type');
var customers_type_value;
for (var i = 0; i < customersType.length; i++) {
    if (customersType[i].checked) {
        customers_type_value = customersType[i].value;
    }
}
// alert(customers_type_value);

// 2. Категория транспорта: мото или авто
var vehicleType = document.getElementsByName('vehicle_type');
var vehicle_type_value;
for (var i = 0; i < vehicleType.length; i++) {
    if (vehicleType[i].checked){
        vehicle_type_value = vehicleType[i].value;
    }
}
// alert(vehicle_type_value);

// 3. Категория по типу двигателя: бензин, дизель, электро
var engine_type = document.getElementsByName('engine_type');
var engine_type_value;
for (var i = 0; i < engine_type.length; i++) {
    if (engine_type[i].checked){
        engine_type_value = engine_type[i].value;
    }
}
// alert(engine_type_value);

// 4. Таможенная льгота 50% (указ №140): да, нет
var decree_140 = document.getElementsByName('decree_140');
var decree_140_value;
for (var i = 0; i < decree_140.length; i++) {
    if (decree_140[i].checked){
        decree_140_value = decree_140[i].value;
    }
}
// alert(decree_140_value);

/* ТЕКУЩИЙ ГОД */
const actualYear = 2021

/* Значения из input type="number" */
var vehicleAgeInput3N = document.getElementById('input_4_vehicle_age'),
    vehiclePriceInput4N = document.getElementById('input_5_vehicle_price'),
    engineVolumeInput5N = document.getElementById('input_6_engine_volume');

/* Итоговое значение */
var totalAmountOfFee = document.getElementById('out-result');

//a = 2
//b = 2
//if (customers_type_value == 'Физическое лицо') {
//    document.querySelector('.out-result').innerHTML = 'Физическое лицо';
//} else if (customers_type_value == 'Юридическое лицо') {
//    document.querySelector('.out-result').innerHTML = 'Юридическое лицо';
//}
//var ev = document.getElementById("evaluate");
//ev.onclick = function () {
//    if (document.getElementById('input_1_customers_type').checked == true){
//        document.querySelector('.out-result').innerHTML = 'Физическое лицо';
//    } else if (document.getElementById('input_2_customers_type').checked == true) {
//        document.querySelector('.out-result').innerHTML = 'Юридическое лицо';
//    }
//}

var ev = document.getElementById("evaluate");
ev.onclick = function () {
    if (document.getElementById('input_1_customers_type').checked == true) // ФЛ
    {
        if (document.getElementById('input_1_vehicle_type').checked == true) // Мотоцикл
        {
            if (document.getElementById('input_2_engine_type').checked == true) // Бензин
            {
                if (document.getElementById('input_6_engine_volume').value <= 50) // Объем двигателя
                {
                    var moto_price = document.getElementById('input_5_vehicle_price').value * 0.14;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                    "<span style='color:red'>" + "<strong>" + moto_price + " " + "&#8364;"+ "</strong>"
                    + "</span>" + ".";
                } else if (document.getElementById('input_6_engine_volume').value > 50 &&
                    document.getElementById('input_6_engine_volume').value <= 250)
                {
                    var moto_price = document.getElementById('input_5_vehicle_price').value * 0.14;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                    "<span style='color:red'>" + "<strong>" + moto_price + " " + "&#8364;"+ "</strong>"
                     + "</span>" + ".";
                } else if (document.getElementById('input_6_engine_volume').value > 250 &&
                    document.getElementById('input_6_engine_volume').value <= 500)
                {
                    var moto_price = document.getElementById('input_5_vehicle_price').value * 0.15;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + moto_price + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_6_engine_volume').value > 500 &&
                    document.getElementById('input_6_engine_volume').value <= 800)
                {
                    var moto_price = document.getElementById('input_5_vehicle_price').value * 0.15;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + moto_price + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_6_engine_volume').value > 800)
                {
                    var moto_price = document.getElementById('input_5_vehicle_price').value * 0.10;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + moto_price + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                }
            } else if (document.getElementById('input_3_engine_type').checked == true)
            {
                var moto_price = "Дизельные мотоциклы — большая редкость в наши дни. :)";
                document.querySelector('.out-result').innerHTML = moto_price;
                //document.write('.out-result').innerHTML = "Дизельные мотоциклы — большая редкость в наши дни.";
            }
        } else if (document.getElementById('input_2_vehicle_type').checked == true) // Автомобиль
        {
            if (actualYear - document.getElementById('input_4_vehicle_age').value < 3) // Менее 3-х лет
            {
                if (document.getElementById('input_5_vehicle_price').value <= 8500)
                {
                    var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.54),
                    (document.getElementById('input_6_engine_volume').value * 2.5))
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_5_vehicle_price').value >= 8501 &&
                 document.getElementById('input_5_vehicle_price').value <= 16700)
                {
                    var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.48),
                    (document.getElementById('input_6_engine_volume').value * 3.5))
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_5_vehicle_price').value >= 16701 &&
                 document.getElementById('input_5_vehicle_price').value <= 42300)
                {
                    var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.48),
                    (document.getElementById('input_6_engine_volume').value * 5.5))
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_5_vehicle_price').value >= 42301 &&
                 document.getElementById('input_5_vehicle_price').value <= 84500)
                {
                    var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.48),
                    (document.getElementById('input_6_engine_volume').value * 7.5))
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_5_vehicle_price').value >= 84501 &&
                 document.getElementById('input_5_vehicle_price').value <= 169000)
                {
                    var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.48),
                    (document.getElementById('input_6_engine_volume').value * 15))
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_5_vehicle_price').value >= 169001)
                {
                    var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.48),
                    (document.getElementById('input_6_engine_volume').value * 20))
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                }
            } else if (actualYear - document.getElementById('input_4_vehicle_age').value >= 3 &&
             actualYear - document.getElementById('input_4_vehicle_age').value < 5) // От 3-х до 5 лет
            {
                if (document.getElementById('input_6_engine_volume').value <= 1000)
                {
                    var autoAmountFee = document.getElementById('input_6_engine_volume').value * 1.5;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_6_engine_volume').value >= 1001 &&
                document.getElementById('input_6_engine_volume').value <= 1500)
                {
                    var autoAmountFee = document.getElementById('input_6_engine_volume').value * 1.7;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_6_engine_volume').value >= 1501 &&
                document.getElementById('input_6_engine_volume').value <= 1800)
                {
                    var autoAmountFee = document.getElementById('input_6_engine_volume').value * 2.5;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_6_engine_volume').value >= 1801 &&
                document.getElementById('input_6_engine_volume').value <= 2300)
                {
                    var autoAmountFee = document.getElementById('input_6_engine_volume').value * 2.7;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_6_engine_volume').value >= 2301 &&
                document.getElementById('input_6_engine_volume').value < 3000)
                {
                    var autoAmountFee = document.getElementById('input_6_engine_volume').value * 3.0;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_6_engine_volume').value >= 3000)
                {
                    var autoAmountFee = document.getElementById('input_6_engine_volume').value * 3.6;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                }
            } else if (actualYear - document.getElementById('input_4_vehicle_age').value >= 5) // Более 5 лет
             {
                if (document.getElementById('input_6_engine_volume').value <= 1000)
                {
                    var autoAmountFee = document.getElementById('input_6_engine_volume').value * 3.0;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_6_engine_volume').value >= 1001 &&
                document.getElementById('input_6_engine_volume').value <= 1500)
                {
                    var autoAmountFee = document.getElementById('input_6_engine_volume').value * 3.2;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_6_engine_volume').value >= 1501 &&
                document.getElementById('input_6_engine_volume').value <= 1800)
                {
                    var autoAmountFee = document.getElementById('input_6_engine_volume').value * 3.5;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_6_engine_volume').value >= 1801 &&
                document.getElementById('input_6_engine_volume').value <= 2300)
                {
                    var autoAmountFee = document.getElementById('input_6_engine_volume').value * 4.8;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_6_engine_volume').value >= 2301 &&
                document.getElementById('input_6_engine_volume').value < 3000)
                {
                    var autoAmountFee = document.getElementById('input_6_engine_volume').value * 5.0;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_6_engine_volume').value >= 3000)
                {
                    var autoAmountFee = document.getElementById('input_6_engine_volume').value * 5.7;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                }
             }
        }
    } else if (document.getElementById('input_2_customers_type').checked == true) // ЮЛ
    {
        if (document.getElementById('input_1_vehicle_type').checked == true) // Мотоцикл  !!!!!!!!!!!!!!!!!!!!!!!!!!!!
        {
            // Добавить код по алгоритму растаможки мотоцикла ЧЕРЕЗ ЮЛ (аналогичен ФЛ)
            if (document.getElementById('input_2_engine_type').checked == true) // Бензин
            {
                if (document.getElementById('input_6_engine_volume').value <= 50) // Объем двигателя
                {
                    var moto_price = document.getElementById('input_5_vehicle_price').value * 0.14;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                    "<span style='color:red'>" + "<strong>" + moto_price + " " + "&#8364;"+ "</strong>"
                    + "</span>" + ".";
                } else if (document.getElementById('input_6_engine_volume').value > 50 &&
                    document.getElementById('input_6_engine_volume').value <= 250)
                {
                    var moto_price = document.getElementById('input_5_vehicle_price').value * 0.14;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                    "<span style='color:red'>" + "<strong>" + moto_price + " " + "&#8364;"+ "</strong>"
                     + "</span>" + ".";
                } else if (document.getElementById('input_6_engine_volume').value > 250 &&
                    document.getElementById('input_6_engine_volume').value <= 500)
                {
                    var moto_price = document.getElementById('input_5_vehicle_price').value * 0.15;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + moto_price + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_6_engine_volume').value > 500 &&
                    document.getElementById('input_6_engine_volume').value <= 800)
                {
                    var moto_price = document.getElementById('input_5_vehicle_price').value * 0.15;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + moto_price + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                } else if (document.getElementById('input_6_engine_volume').value > 800)
                {
                    var moto_price = document.getElementById('input_5_vehicle_price').value * 0.10;
                    document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + moto_price + " " + "&#8364;"+ "</strong>"
                      + "</span>" + ".";
                }
            } else if (document.getElementById('input_3_engine_type').checked == true)
            {
                var moto_price = "Дизельные мотоциклы — большая редкость в наши дни. :)";
                document.querySelector('.out-result').innerHTML = moto_price;
                //document.write('.out-result').innerHTML = "Дизельные мотоциклы — большая редкость в наши дни.";
            }  // Мотоцикл  !!!!!!!!!!!!!!!!!!!!!!!!!!!!

        } else if (document.getElementById('input_2_vehicle_type').checked == true) // Автомобиль
        {
            if (document.getElementById('input_2_engine_type').checked == true) // Бензин
            {
                if (actualYear - document.getElementById('input_4_vehicle_age').value < 3) // Менее 3-х лет
                {
                    if (document.getElementById('input_6_engine_volume').value <= 1000)
                    {
                        var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.3),
                         (document.getElementById('input_6_engine_volume').value * 1.2))
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 1001 &&
                    document.getElementById('input_6_engine_volume').value <= 1500)
                    {
                        var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.3),
                         (document.getElementById('input_6_engine_volume').value * 1.45))
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 1501 &&
                    document.getElementById('input_6_engine_volume').value <= 1800)
                    {
                        var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.3),
                         (document.getElementById('input_6_engine_volume').value * 1.5))
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 1801 &&
                    document.getElementById('input_6_engine_volume').value <= 2300)
                    {
                        var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.3),
                         (document.getElementById('input_6_engine_volume').value * 2.15))
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 2301 &&
                    document.getElementById('input_6_engine_volume').value < 3000)
                    {
                        var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.3),
                         (document.getElementById('input_6_engine_volume').value * 2.15))
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 3000)
                    {
                        var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.3),
                         (document.getElementById('input_6_engine_volume').value * 2.8))
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    }
                } else if (actualYear - document.getElementById('input_4_vehicle_age').value >= 3 &&
                 actualYear - document.getElementById('input_4_vehicle_age').value < 5) // От 3-х до 5 лет
                {
                    if (document.getElementById('input_6_engine_volume').value <= 1000)
                    {
                        var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.35),
                         (document.getElementById('input_6_engine_volume').value * 1.2))
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 1001 &&
                    document.getElementById('input_6_engine_volume').value <= 1500)
                    {
                        var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.35),
                         (document.getElementById('input_6_engine_volume').value * 1.45))
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 1501 &&
                    document.getElementById('input_6_engine_volume').value <= 1800)
                    {
                        var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.35),
                         (document.getElementById('input_6_engine_volume').value * 1.5))
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 1801 &&
                    document.getElementById('input_6_engine_volume').value <= 2300)
                    {
                        var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.35),
                         (document.getElementById('input_6_engine_volume').value * 2.15))
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 2301 &&
                    document.getElementById('input_6_engine_volume').value < 3000)
                    {
                        var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.35),
                         (document.getElementById('input_6_engine_volume').value * 2.15))
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 3000)
                    {
                        var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.35),
                         (document.getElementById('input_6_engine_volume').value * 2.8))
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    }
                } else if (actualYear - document.getElementById('input_4_vehicle_age').value >= 5) // Более 5 лет
                {
                    if (document.getElementById('input_6_engine_volume').value <= 1000)
                    {
                        var autoAmountFee = document.getElementById('input_6_engine_volume').value * 2.5;
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 1001 &&
                    document.getElementById('input_6_engine_volume').value <= 1500)
                    {
                        var autoAmountFee = document.getElementById('input_6_engine_volume').value * 2.7;
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 1501 &&
                    document.getElementById('input_6_engine_volume').value <= 1800)
                    {
                        var autoAmountFee = document.getElementById('input_6_engine_volume').value * 2.9;
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 1801 &&
                    document.getElementById('input_6_engine_volume').value <= 2300)
                    {
                        var autoAmountFee = document.getElementById('input_6_engine_volume').value * 4.0;
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 2301 &&
                    document.getElementById('input_6_engine_volume').value < 3000)
                    {
                        var autoAmountFee = document.getElementById('input_6_engine_volume').value * 4.0;
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 3000)
                    {
                        var autoAmountFee = document.getElementById('input_6_engine_volume').value * 5.8;
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    }
                }
            } else if (document.getElementById('input_3_engine_type').checked == true) // Дизель
            {
                if (actualYear - document.getElementById('input_4_vehicle_age').value < 3) // Менее 3-х лет
                {
                    if (document.getElementById('input_6_engine_volume').value <= 1500)
                    {
                        var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.3),
                         (document.getElementById('input_6_engine_volume').value * 1.45))
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 1501 &&
                    document.getElementById('input_6_engine_volume').value <= 2500)
                    {
                        var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.3),
                         (document.getElementById('input_6_engine_volume').value * 1.9))
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 2501)
                    {
                        var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.3),
                         (document.getElementById('input_6_engine_volume').value * 2.8))
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    }
                } else if (actualYear - document.getElementById('input_4_vehicle_age').value >= 3 &&
                 actualYear - document.getElementById('input_4_vehicle_age').value < 5) // От 3-х до 5 лет
                {
                    if (document.getElementById('input_6_engine_volume').value <= 1500)
                    {
                        var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.35),
                         (document.getElementById('input_6_engine_volume').value * 1.45))
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 1501 &&
                    document.getElementById('input_6_engine_volume').value <= 2500)
                    {
                        var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.35),
                         (document.getElementById('input_6_engine_volume').value * 2.15))
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 2501)
                    {
                        var autoAmountFee = Math.max((document.getElementById('input_5_vehicle_price').value * 0.35),
                         (document.getElementById('input_6_engine_volume').value * 2.8))
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    }
                } else if (actualYear - document.getElementById('input_4_vehicle_age').value >= 5) // Более 5 лет
                {
                    if (document.getElementById('input_6_engine_volume').value <= 1500)
                    {
                        var autoAmountFee = document.getElementById('input_6_engine_volume').value * 2.7;
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 1501 &&
                    document.getElementById('input_6_engine_volume').value <= 2500)
                    {
                        var autoAmountFee = document.getElementById('input_6_engine_volume').value * 4.0;
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    } else if (document.getElementById('input_6_engine_volume').value >= 2501)
                    {
                        var autoAmountFee = document.getElementById('input_6_engine_volume').value * 5.8;
                        document.querySelector('.out-result').innerHTML = 'Растаможка составит: ' +
                     "<span style='color:red'>" + "<strong>" + autoAmountFee + " " + "&#8364;" + "</strong>"
                      + "</span>" + ".";
                    }
                }
            }
        }
    }
}
