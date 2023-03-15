function show_value2(x)
{
 document.getElementById("slider_value2").innerHTML=x;
}
function add_one()
{
    document.getElementById("myrange").value =parseInt(document.getElementById("myrange").value)+1;
  show_value2(document.getElementById("myrange").value);
}
function subtract_one()
{
    document.getElementById("myrange").value =parseInt(document.getElementById("myrange").value)-1;
    show_value2(document.getElementById("myrange").value);
}
