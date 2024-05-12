import React, {useEffect, useState} from "react";
import axios from "axios";

function Comments() {
    const URL_COMMENTS = "http://localhost:8000/palavrao/api/comments/"; // (1)
    const [commentList, setCommentsList] = useState([]); // (2)
    const getComments = () => { // (3)
        axios.get(URL_COMMENTS)
            .then((request) => {
                setCommentsList(request.data)
            });
    };
    useEffect(() => { //(4)
        getComments();
    }, []);

    return (
        <>
            <br/>
            <div style={{textAlign: "center"}}>
                <h2 style={{fontFamily: "Arial, sans-serif", color: "#333"}}>Comentários do Palavrão:</h2>
            </div>
            <div className="comments-container" id="comments-container" style={{textAlign: "center"}}>
                {commentList.length > 0 ? (
                    commentList.map((comment) => (
                        <div key={comment.pk} className="comment-item">
                            <p>
                                <a style={{fontSize: `${comment.size}px`}}>{comment.text}</a>
                            </p>
                        </div>
                    ))
                ) : (
                    <p>Nenhum comentário encontrado.</p>
                )}
            </div>
        </>
    );
}

export default Comments