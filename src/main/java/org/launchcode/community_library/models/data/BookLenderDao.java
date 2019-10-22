package org.launchcode.community_library.models.data;

import org.launchcode.community_library.models.BookLender;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

@Repository
@Transactional
public interface BookLenderDao extends CrudRepository<BookLender,Integer > {
}
