import React, { Component } from "react";
import SelectSongsPage from "./SelectSongsPage";
import PlaylistCreatedPage from "./PlaylistCreatedPage";
import { BrowserRouter, Routes, Route, Link, Redirect } from "react-router-dom"

export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <BrowserRouter>
                <Routes>
                    <Route exact path="/" element={
                        <p>This is the Home Page!</p>
                    }>  
                    </Route>
                    <Route path="/selectsongs" element={<SelectSongsPage />}/>
                    <Route path="/playlistcreated" element={<PlaylistCreatedPage />}/>
                </Routes>
            </BrowserRouter>
        );
    }
}