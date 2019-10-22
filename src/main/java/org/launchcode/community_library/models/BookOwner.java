package org.launchcode.community_library.models;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Entity
public class BookOwner {
    @Id
    @GeneratedValue
    private int id;
    private String firstName;
    private String lastName;
    @ManyToOne
    @JoinColumn(name="book_id")
    private Book book;

    @Embedded
    private  Address address;

    public  BookOwner(){}

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Book getBook() {
        return book;
    }

    public void setBook(Book book) {
        this.book = book;
    }
}
