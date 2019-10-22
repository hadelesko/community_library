package org.launchcode.community_library.models;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

@Entity
public class Bookhub {
    @Id
    @GeneratedValue
    private int id;
    private Address address;
    @ManyToOne
    private Book book;

    public Bookhub(){}
}
