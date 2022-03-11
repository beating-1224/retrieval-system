import axios from "axios"
// import Qs from 'qs'

const api = {
    getDatasets() {
        return axios.get("/api/datasets");
    },
    // getDatasets(params) {
    //     let readyData = Qs.stringify({
    //         username: params.username,
    //         password: params.password,
    //         email: params.email
    //     });
    //     return axios.post("/api/v1/register", readyData);
    // },
    getSamples(datasets) {
        return axios.get("/api/samples", { params: { datasets: datasets } })
    },
    search(query,datasets, modalities){
        return axios.get("/api/search_sample", { params: { query: query,datasets:datasets,modalities:modalities} })
    }
}

export default api;