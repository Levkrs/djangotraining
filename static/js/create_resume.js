'use strict'
const status = document.getElementById('form_for_post')
const to_draft_btn = document.getElementById("to_draft")
const submit_btn = document.getElementById("submit_button")
// let status_click = false


to_draft_btn.addEventListener("click",function () {
    console.log("Click to_draft")
    // status_click = true;
    submit_btn.click()
})


// document.getElementById("to_draft").addEventListener("click", function(e) {
//         console.log("CLick")
//
//         console.log($('form_for_post').serialize())
//         // $("form_for_post").each(function () {
//         //     console.log(data)
//             // data[theFieldName] = theFieldValue;
// // });
//
//
// });
//
// /*
//     On submiting the form, send the POST ajax
//     request to server and after successfull submission
//     display the object.
// */
// $("#form_for_post").submit(function (e) {
//     // console.log("status_clicker", status_clicker)
//     // preventing from page reload and default actions
//     e.preventDefault();
//
//
//     // serialize the data for sending the form data.
//     var serializedData = $(this).serialize();
//     serializedData = serializedData + "=&status=2"
//     this.data = serializedData
//     console.log(serializedData)
//     // console.log($(data))
//     console.log(typeof(serializedData))
//     console.log(this.data)
//     // $(this).unbind('submit').submit()
//     // submit_btn.click()
//
//
//     // make POST ajax call
//     $.ajax({
//         type: 'POST',
//         url: "{% url 'post_friend' %}",
//         data: serializedData,
//         success: function (response) {
//             // on successfull creating object
//             // 1. clear the form.
//             $("#friend-form").trigger('reset');
//             // 2. focus to nickname input
//             $("#id_nick_name").focus();
//
//             // display the newly friend to table.
//             var instance = JSON.parse(response["instance"]);
//             var fields = instance[0]["fields"];
//             $("#my_friends tbody").prepend(
//                 `<tr>
//                     <td>${fields["nick_name"] || ""}</td>
//                     <td>${fields["first_name"] || ""}</td>
//                     <td>${fields["last_name"] || ""}</td>
//                     <td>${fields["likes"] || ""}</td>
//                     <td>${fields["dob"] || ""}</td>
//                     <td>${fields["lives_in"] || ""}</td>
//                     </tr>`
//             )
//         },
//         error: function (response) {
//             // alert the error if any error occured
//             alert(response["responseJSON"]["error"]);
//         }
//     })
// })




