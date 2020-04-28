let darasas = [{
        id: 1,
        title: 'The first post',
        slug: 'first-post',
        exerpt: 'The first post exerpt',
        content: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore temporibus officia voluptatum reiciendis, illo ex iste molestias, doloremque! Laboriosam nihil sit, tempora nam porro placeat reprehenderit non exercitationem ipsa magnam!'
    },
    {
        id: 2,
        title: 'The second post',
        slug: 'second-post',
        exerpt: 'The second post exerpt',
        content: 'Consectetur adipisicing elit. Inventore temporibus officia voluptatum reiciendis, illo ex iste molestias, doloremque! Laboriosam nihil sit, tempora nam porro placeat reprehenderit non exercitationem ipsa magnam!'
    },
];
const url = "http://127.0.0.1:8000/darasa_list";

let Home = {
    template: `
<div>
	<h1 class="page-header">Home</h1>
	<div v-for="darasa in darasas">
		<h3><router-link :to="/darasas/ + darasa.slug">{{ darasa.title }}</router-link></h3>
		<p>{{ darasa.exerpt }}</p>
	</div>
</div>
	`,

    data() {
        return {
            darasas: []
        }
    },

    mounted() {
        this.darasas = darasas;
    }
};

let Contact = {
    template: `
		<div>
			<h1 class="page-header">Contact</h1>
			<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quaerat eos suscipit molestias nam numquam ratione aliquid provident id earum ipsam omnis, temporibus vero porro molestiae, facilis tempora itaque libero mollitia voluptatum, architecto ad! Sit alias aut provident amet pariatur accusantium voluptates! Tempora cumque reprehenderit dicta molestiae nulla quam reiciendis cum nam aliquam corporis, dolor modi, sunt ipsam. Obcaecati veritatis illum rem vel tempore, explicabo voluptates id incidunt quod laborum tempora inventore aut alias culpa laboriosam non, ducimus rerum repellendus voluptatem beatae soluta consequuntur, repellat aspernatur. Atque incidunt velit eius libero, molestiae eos delectus error distinctio minima laboriosam quasi earum expedita fugit quos? Recusandae molestiae ipsum quasi? Explicabo dolorum neque quam dolorem, non assumenda iusto, atque tenetur odio sequi quis incidunt.</p>
		</div>
	`
};

let Darasa = {
    template: `
		<div>
			<h2>{{ darasa.title }}</h2>
			<p>{{ darasa.content }}</p>
		</div>
	`,

    data() {
        return {
            darasa: {}
        };
    },

    mounted() {
        this.darasa = this.findBySlug(this.$route.params.slug);
    },

    methods: {
        findBySlug(slug) {
            for (let i = 0; i < darasas.length; i++) {
                if (slug === darasas[i].slug) return darasas[i];
            }

            return null;
        }
    }
};
let Curricula = {
    template: `
    <div class="row" v-for="result in results" v-bind:key="result.id">
        <p><a class="nav-link text-black font-weight-bold" href="#">{{ result.title }}$</a></p>
    </div>
    `,

     data: {
             results: []
         },
         mounted() {
             axios.get(url).then(response => {
                 this.results = response.data
             })
         }

     };

let routes = [{
        path: '/',
        component: Home
    },
    {
        path: '/contact',
        component: Contact
    },
    {
        path: '/curricula',
        component: Curricula
    },
    {
        path: '/darasas/:slug',
        component: Darasa
    }
];

let router = new VueRouter({
    delimiters: ['${', '}$'],
    routes
});

let app = new Vue({
    router
}).$mount('#app');