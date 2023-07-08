import React, {useState, useEffect} from "react";
import './Post.css'

const BASE_URL = 'http://localhost:8080/'

function Post({post}){
    const [imageUrl, setImageUrl] = useState('')

    useEffect(() => {
        setImageUrl(BASE_URL + post.IMAGE_URL);
    }, [])

    return (
        <div className="post">
            <img className="post_image" src={imageUrl}/>
        </div>
    )
}

export default Post