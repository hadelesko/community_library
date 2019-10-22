package org.launchcode.community_library.models.data;

import org.launchcode.community_library.models.Member;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

@Repository
@Transactional
public interface BookTransaction extends CrudRepository<Member, Integer> {
}
