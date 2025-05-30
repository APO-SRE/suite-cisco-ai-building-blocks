from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.common_rest_error import CommonRestError
from ...models.config_get_fabric_candidates_response import ConfigGetFabricCandidatesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    fabric_id: str,
    *,
    name: Union[Unset, str] = UNSET,
    txn_id: Union[Unset, int] = UNSET,
    need_inactive: Union[Unset, bool] = UNSET,
    need_reviews: Union[Unset, bool] = UNSET,
    need_events: Union[Unset, bool] = UNSET,
    start_time: Union[Unset, str] = UNSET,
    end_time: Union[Unset, str] = UNSET,
    pagination_limit: Union[Unset, int] = UNSET,
    pagination_cursor: Union[Unset, str] = UNSET,
    pagination_sort_by: Union[Unset, str] = UNSET,
    pagination_sort_desc: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name"] = name

    params["txnId"] = txn_id

    params["needInactive"] = need_inactive

    params["needReviews"] = need_reviews

    params["needEvents"] = need_events

    params["startTime"] = start_time

    params["endTime"] = end_time

    params["pagination.limit"] = pagination_limit

    params["pagination.cursor"] = pagination_cursor

    params["pagination.sortBy"] = pagination_sort_by

    params["pagination.sortDesc"] = pagination_sort_desc

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/fabrics/{fabric_id}/candidates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CommonRestError, ConfigGetFabricCandidatesResponse]]:
    if response.status_code == 200:
        response_200 = ConfigGetFabricCandidatesResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = CommonRestError.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = CommonRestError.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = CommonRestError.from_dict(response.json())

        return response_403
    if response.status_code == 429:
        response_429 = CommonRestError.from_dict(response.json())

        return response_429
    if response.status_code == 500:
        response_500 = CommonRestError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CommonRestError, ConfigGetFabricCandidatesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fabric_id: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    txn_id: Union[Unset, int] = UNSET,
    need_inactive: Union[Unset, bool] = UNSET,
    need_reviews: Union[Unset, bool] = UNSET,
    need_events: Union[Unset, bool] = UNSET,
    start_time: Union[Unset, str] = UNSET,
    end_time: Union[Unset, str] = UNSET,
    pagination_limit: Union[Unset, int] = UNSET,
    pagination_cursor: Union[Unset, str] = UNSET,
    pagination_sort_by: Union[Unset, str] = UNSET,
    pagination_sort_desc: Union[Unset, bool] = UNSET,
) -> Response[Union[CommonRestError, ConfigGetFabricCandidatesResponse]]:
    """Get the list of candidate configurations information in a fabric.

    Args:
        fabric_id (str):
        name (Union[Unset, str]):
        txn_id (Union[Unset, int]):
        need_inactive (Union[Unset, bool]):
        need_reviews (Union[Unset, bool]):
        need_events (Union[Unset, bool]):
        start_time (Union[Unset, str]):
        end_time (Union[Unset, str]):
        pagination_limit (Union[Unset, int]):
        pagination_cursor (Union[Unset, str]):
        pagination_sort_by (Union[Unset, str]):
        pagination_sort_desc (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, ConfigGetFabricCandidatesResponse]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        name=name,
        txn_id=txn_id,
        need_inactive=need_inactive,
        need_reviews=need_reviews,
        need_events=need_events,
        start_time=start_time,
        end_time=end_time,
        pagination_limit=pagination_limit,
        pagination_cursor=pagination_cursor,
        pagination_sort_by=pagination_sort_by,
        pagination_sort_desc=pagination_sort_desc,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fabric_id: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    txn_id: Union[Unset, int] = UNSET,
    need_inactive: Union[Unset, bool] = UNSET,
    need_reviews: Union[Unset, bool] = UNSET,
    need_events: Union[Unset, bool] = UNSET,
    start_time: Union[Unset, str] = UNSET,
    end_time: Union[Unset, str] = UNSET,
    pagination_limit: Union[Unset, int] = UNSET,
    pagination_cursor: Union[Unset, str] = UNSET,
    pagination_sort_by: Union[Unset, str] = UNSET,
    pagination_sort_desc: Union[Unset, bool] = UNSET,
) -> Optional[Union[CommonRestError, ConfigGetFabricCandidatesResponse]]:
    """Get the list of candidate configurations information in a fabric.

    Args:
        fabric_id (str):
        name (Union[Unset, str]):
        txn_id (Union[Unset, int]):
        need_inactive (Union[Unset, bool]):
        need_reviews (Union[Unset, bool]):
        need_events (Union[Unset, bool]):
        start_time (Union[Unset, str]):
        end_time (Union[Unset, str]):
        pagination_limit (Union[Unset, int]):
        pagination_cursor (Union[Unset, str]):
        pagination_sort_by (Union[Unset, str]):
        pagination_sort_desc (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, ConfigGetFabricCandidatesResponse]
    """

    return sync_detailed(
        fabric_id=fabric_id,
        client=client,
        name=name,
        txn_id=txn_id,
        need_inactive=need_inactive,
        need_reviews=need_reviews,
        need_events=need_events,
        start_time=start_time,
        end_time=end_time,
        pagination_limit=pagination_limit,
        pagination_cursor=pagination_cursor,
        pagination_sort_by=pagination_sort_by,
        pagination_sort_desc=pagination_sort_desc,
    ).parsed


async def asyncio_detailed(
    fabric_id: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    txn_id: Union[Unset, int] = UNSET,
    need_inactive: Union[Unset, bool] = UNSET,
    need_reviews: Union[Unset, bool] = UNSET,
    need_events: Union[Unset, bool] = UNSET,
    start_time: Union[Unset, str] = UNSET,
    end_time: Union[Unset, str] = UNSET,
    pagination_limit: Union[Unset, int] = UNSET,
    pagination_cursor: Union[Unset, str] = UNSET,
    pagination_sort_by: Union[Unset, str] = UNSET,
    pagination_sort_desc: Union[Unset, bool] = UNSET,
) -> Response[Union[CommonRestError, ConfigGetFabricCandidatesResponse]]:
    """Get the list of candidate configurations information in a fabric.

    Args:
        fabric_id (str):
        name (Union[Unset, str]):
        txn_id (Union[Unset, int]):
        need_inactive (Union[Unset, bool]):
        need_reviews (Union[Unset, bool]):
        need_events (Union[Unset, bool]):
        start_time (Union[Unset, str]):
        end_time (Union[Unset, str]):
        pagination_limit (Union[Unset, int]):
        pagination_cursor (Union[Unset, str]):
        pagination_sort_by (Union[Unset, str]):
        pagination_sort_desc (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, ConfigGetFabricCandidatesResponse]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        name=name,
        txn_id=txn_id,
        need_inactive=need_inactive,
        need_reviews=need_reviews,
        need_events=need_events,
        start_time=start_time,
        end_time=end_time,
        pagination_limit=pagination_limit,
        pagination_cursor=pagination_cursor,
        pagination_sort_by=pagination_sort_by,
        pagination_sort_desc=pagination_sort_desc,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fabric_id: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    txn_id: Union[Unset, int] = UNSET,
    need_inactive: Union[Unset, bool] = UNSET,
    need_reviews: Union[Unset, bool] = UNSET,
    need_events: Union[Unset, bool] = UNSET,
    start_time: Union[Unset, str] = UNSET,
    end_time: Union[Unset, str] = UNSET,
    pagination_limit: Union[Unset, int] = UNSET,
    pagination_cursor: Union[Unset, str] = UNSET,
    pagination_sort_by: Union[Unset, str] = UNSET,
    pagination_sort_desc: Union[Unset, bool] = UNSET,
) -> Optional[Union[CommonRestError, ConfigGetFabricCandidatesResponse]]:
    """Get the list of candidate configurations information in a fabric.

    Args:
        fabric_id (str):
        name (Union[Unset, str]):
        txn_id (Union[Unset, int]):
        need_inactive (Union[Unset, bool]):
        need_reviews (Union[Unset, bool]):
        need_events (Union[Unset, bool]):
        start_time (Union[Unset, str]):
        end_time (Union[Unset, str]):
        pagination_limit (Union[Unset, int]):
        pagination_cursor (Union[Unset, str]):
        pagination_sort_by (Union[Unset, str]):
        pagination_sort_desc (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, ConfigGetFabricCandidatesResponse]
    """

    return (
        await asyncio_detailed(
            fabric_id=fabric_id,
            client=client,
            name=name,
            txn_id=txn_id,
            need_inactive=need_inactive,
            need_reviews=need_reviews,
            need_events=need_events,
            start_time=start_time,
            end_time=end_time,
            pagination_limit=pagination_limit,
            pagination_cursor=pagination_cursor,
            pagination_sort_by=pagination_sort_by,
            pagination_sort_desc=pagination_sort_desc,
        )
    ).parsed
