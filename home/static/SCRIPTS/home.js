/* Thêm hoặc xóa class show ra khỏi phần tử */
function myFunction(id) {
    document.getElementById(id).classList.toggle("show");
}
//lấy tất cả các button menu
var buttons = document.getElementsByClassName('dropbtn');
//lấy tất cả các thẻ chứa menu con
var contents = document.getElementsByClassName('dropdown-content');
//lặp qua tất cả các button menu và gán sự kiện
for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", function(){
        //lấy value của button
        var id = this.value;
        //ẩn tất cả các menu con đang được hiển thị
        for (var i = 0; i < contents.length; i++) {
            contents[i].classList.remove("show");
        }
        //hiển thị menu vừa được click
        myFunction(id);
    });
}
//nếu click ra ngoài các button thì ẩn tất cả các menu con
window.addEventListener("click", function(){
     if (!event.target.matches('.dropbtn')){
        for (var i = 0; i < contents.length; i++) {
            contents[i].classList.remove("show");
        }
     }
});