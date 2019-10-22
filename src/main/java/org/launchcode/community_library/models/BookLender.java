package org.launchcode.community_library.models;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Entity
public class BookLender {
    @Id
    @GeneratedValue
    private int id;
    private String firstName;
    private String lastName;
    @Embedded
    private  Address address;

    @OneToMany(mappedBy="bookLender")
    private Set<Book> lentBooks= new HashSet<Book>();

    public BookLender(){}

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public Address getAddress() {
        return address;
    }

    public void setAddress(Address address) {
        this.address = address;
    }

    public Set<Book> getLentBooks() {
        return lentBooks;
    }

    public void setLentBooks(Set<Book> lentBooks) {
        this.lentBooks = lentBooks;
    }
}
