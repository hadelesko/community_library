package org.launchcode.community_library.models;

import javax.persistence.*;
import java.util.*;
@Entity
public class Member_BookHub { //Transactions member and library
    @Id
    @GeneratedValue
    private int transaction_id;
    /*
    To get the book_id, member_id, bookHub_id i will need to
    add list of  objects Member, Book, BookHub as selectable list
    to the add template of Member_BookHub and add in the Controller
    -memberDao.findAll() for members to get member_id
    -bookDao.findAll() for books to get book_id
    -bookHubDao.findAll() for bookHubs to get bookHub_id
    */
    private int book_id;
    //private Set<Book>books =new HashSet<Book>();
    private int member_id;
    private int bookHub_id;

    @Temporal(TemporalType.DATE)
    private Date startDate;

    @Temporal(TemporalType.DATE)
    private Date endDate;

    @OneToMany(mappedBy="member_bookHub") //== the members will be hold by the table book_transaction
    private Set<Member>memberList=new HashSet<>();

    public Member_BookHub(){}

    public int getTransaction_id() {
        return transaction_id;
    }

    public void setTransaction_id(int transaction_id) {
        this.transaction_id = transaction_id;
    }

    public int getBook_id() {
        return book_id;
    }

    public void setBook_id(int book_id) {
        this.book_id = book_id;
    }

    public int getMember_id() {
        return member_id;
    }

    public void setMember_id(int member_id) {
        this.member_id = member_id;
    }

    public int getBookHub_id() {
        return bookHub_id;
    }

    public void setBookHub_id(int bookHub_id) {
        this.bookHub_id = bookHub_id;
    }

    public Date getStartDate() {
        return startDate;
    }

    public void setStartDate(Date startDate) {
        this.startDate = startDate;
    }

    public Date getEndDate() {
        return endDate;
    }

    public void setEndDate(Date endDate) {
        this.endDate = endDate;
    }

    public Set<Member> getMemberList() {
        return memberList;
    }

    public void setMemberList(Set<Member> memberList) {
        this.memberList = memberList;
    }
}
