package org.launchcode.community_library.models;

import javax.persistence.*;

@Entity
public class Member {
    @Id
    @GeneratedValue
    private int id;

    private String firstName;

    private String lastName;

    @Embedded
    private Address address;
    //member is the owner of the relationship member and member_bookhub
    // and his according to the java persistence the owner of the relationship
    // must be on the many-to-one side
    @ManyToOne
    @JoinColumn(name="member_bookHub_id")
    private Member_BookHub member_bookHub;



    public Member(){}


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

    public Member_BookHub getMember_bookHub() {
        return member_bookHub;
    }

    public void setMember_bookHub(Member_BookHub member_bookHub) {
        this.member_bookHub = member_bookHub;
    }
}
