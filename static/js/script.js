function init() {
  statusList = Array.from(document.querySelectorAll('.status'))
  statusList.forEach(update)
}

function update(item) {
  item.innerText = "offline"
  $.ajax({
    url: '/ping',
    type: 'POST',
    data: item.id,
    success: function(response) {
      item.innerText = response
    }
  })
}

function wake(button) {
  button.innerText = button.id
}
