package org.launchcode.community_library.models;


import javax.persistence.*;
import java.util.Date;
import java.util.HashSet;
import java.util.Set;

@Entity
public class Book {

    @Id
    @GeneratedValue
    private int id;
    private String title;
    private String author;
    private String language;
    private String description;
    @Basic

    private Date editionYear;

    @Temporal(TemporalType.DATE)
    private Date availableDate;
    private Boolean isLent;
    private Boolean isBooked;

    @OneToMany(mappedBy = "book") //One person or book-owner can have
    // or possess many books. By 'mappedBy="book"' we are referring to
    // 'Book book' of the BookOwner-Entity that records the book-owners
    private Set<BookOwner> owners=new HashSet<BookOwner>();

    @ManyToOne//(cascade = {CascadeType.ALL})
    @JoinColumn(name="bookLender_id")
                //Finally the book will have only one lender in a
                // target period because after the  return of
                // the book, the bookLender will be updated
    private BookLender bookLender;

    public Book(){}


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Date getEditionYear() {
        return editionYear;
    }

    public void setEditionYear(Date editionYear) {
        this.editionYear = editionYear;
    }

    public Date getAvailableDate() {
        return availableDate;
    }

    public void setAvailableDate(Date availableDate) {
        this.availableDate = availableDate;
    }

    public Boolean getLent() {
        return isLent;
    }

    public void setLent(Boolean lent) {
        isLent = lent;
    }

    public Boolean getBooked() {
        return isBooked;
    }

    public void setBooked(Boolean booked) {
        isBooked = booked;
    }


    public BookLender getBookLender() {
        return bookLender;
    }

    public void setBookLender(BookLender bookLender) {
        this.bookLender = bookLender;
    }

    public Set<BookOwner> getOwners() {
        return owners;
    }

    public void setOwners(Set<BookOwner> owners) {
        this.owners = owners;
    }
}
