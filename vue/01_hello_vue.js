var app = new Vue({
    el: '#app',
    data: {
        message: 'Привет, Vue!'
    }
})

var app2 = new Vue({
    el: '#app-2',
    data: {
        message: 'Вы загрузили эту страницу: ' + new Date().toLocaleString()
    }
})

var app4 = new Vue({
    el: '#app-4',
    data: {
        todos: [
            { text: 'Изучить JavaScript' },
            { text: 'Изучить Vue' },
            { text: 'Создать что-нибудь классное' }
        ]
    }
})

var app5 = new Vue({
    el: '#app-5',
    data: {
        message: 'Продолжаем!'
    },
    methods: {
        reverseMessage: function() {
            this.message = this.message.split('').reverse().join('')
        }
    }
})


var app6 = new Vue({
    el: '#app-6',
    data: {
        message: 'Связывание формы и состояния приложения'
    }
})


Vue.component('todo-item', {
    props: ['todo'],
    template: '<li>{{ todo.text }}</li>'
})

var app7 = new Vue({
    el: '#app-7',
    data: {
        groceryList: [
            { id: 0, text: 'Овощи' },
            { id: 1, text: 'Сыр' },
            { id: 2, text: 'Что там ещё люди едят?' }
        ]
    }
})